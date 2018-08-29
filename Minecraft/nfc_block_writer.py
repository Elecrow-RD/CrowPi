#!/usr/bin/env python
# Raspberry Pi Minecraft Block NFC Writer
# Author: Tony DiCola
# Copyright (c) 2015 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import signal
import time
import minecraft_blocks as mcpi_data
from pirc522 import RFID
import sys

# Hack to make code compatible with both Python 2 and 3 (since 3 moved
# raw_input from a builtin to a different function, ugh).
try:
    input = raw_input
except NameError:
    pass

# Configure the key to use for writing to the MiFare card.  You probably don't
# need to change this from the default below unless you know your card has a
# different key associated with it.
CARD_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

run = True
rdr = RFID()
util = rdr.util()
util.debug = False

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()

signal.signal(signal.SIGINT, end_read)

print("Starting")

# Step 1, wait for card to be present.
print('Minecraft Block NFC Writer')
print('')
print('== STEP 1 =========================')
print('Place the card to be written on the RC522 NFC Reader/Wrtier...')

while run:
    rdr.wait_for_tag()
    (error, data) = rdr.request()
    if not error:
        print("[-] Card Detected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        print("[-] Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

        print('==============================================================')
        print('WARNING: DO NOT REMOVE CARD FROM RC522 UNTIL FINISHED WRITING!')
        print('==============================================================')
        print('')

        print('== STEP 2 =========================')
        print('Now pick a block type to write to the card.')
        block_choice = None
        while block_choice is None:
            print('')
            print('Type either L to list block types, or type the number of the desired block.')
            print('')
            choice = input('Enter choice (L or block #): ')
            print('')
            if choice.lower() == 'l':
                # Print block numbers and names.
                print('Number\tBlock name')
                print('------\t----------')
                for i, b in enumerate(mcpi_data.BLOCKS):
                    block_name, block_id = b
                    print('{0:>6}\t{1}'.format(i, block_name))
            else:
                # Assume a number must have been entered.
                try:
                    block_choice = int(choice)
                except ValueError:
                    # Something other than a number was entered.  Try again.
                    print('Error! Unrecognized option.')
                    continue
                # Check choice is within bounds of block numbers.
                if not (0 <= block_choice < len(mcpi_data.BLOCKS)):
                    print('Error! Block number must be within 0 to {0}.'.format(len(mcpi_data.BLOCKS)-1))
                    continue
        # Block was chosen, look up its name and ID.
        block_name, block_id = mcpi_data.BLOCKS[block_choice]
        print('You chose the block type: {0}'.format(block_name))
        print('')

        # Get the block subtype if it has any available.
        subtype_choice = None
        if block_name in mcpi_data.SUBTYPES:
            print('Now pick a subtype for the block.')
            print('')
            print('Number\tSubtype')
            print('------\t-------')
            # Print all the subtypes for this block.
            block_subtypes = mcpi_data.SUBTYPES[block_name]
            for subtype_id, subtype_name in block_subtypes.items():
                print('{0:>6}\t{1}'.format(subtype_id, subtype_name))
            # Get a subtype id from the user.
            while subtype_choice is None:
                print('')
                try:
                    subtype_choice = int(input('Enter subtype number: '))
                except ValueError:
                    # Something other than a number was entered.  Try again.
                    print('Error! Unrecognized subtype number.')
                    continue
                if subtype_id not in block_subtypes:
                    print('Error! Subtype number must be one shown above!')
                    continue
        if subtype_choice is not None:
            print('You also chose the subtype: {0}'.format(block_subtypes[subtype_choice]))
            print('')

        # Confirm writing the block type.
        print('== STEP 3 =========================')
        print('Confirm you are ready to write to the card:')
        print('Block: {0}'.format(block_name))
        if subtype_choice is not None:
            print('Subtype: {0}'.format(block_subtypes[subtype_choice]))
        print('')
        choice = input('Confirm card write (Y or N)? ')
        if choice.lower() != 'y' and choice.lower() != 'yes':
            print('Aborted!')
            sys.exit(0)

        print('Writing card (DO NOT REMOVE CARD FROM RC522)...')
        # Write the card!
        # First authenticate block 4.
        util.set_tag(uid)
        # set authorization key
        util.auth(rdr.auth_b, CARD_KEY)
        # rewrite block 4
        util.rewrite(4, [None, None, 0x69, 0x24, 0x40])

        # Next build the data to write to the card.
        # Format is as follows:
        # - Bytes 0-3 are a header with ASCII value 'MCPI'
        # - Byte 4 is the block ID byte
        # - Byte 5 is 0 if block has no subtype or 1 if block has a subtype
        # - Byte 6 is the subtype byte (optional, only if byte 5 is 1)

        data = bytearray(16)
        data[0:4] = b'MCPI'  # Header 'MCPI'
        data[4]   = block_id & 0xFF

        if subtype_choice is not None:
            data[5] = 1
            data[6] = subtype_choice & 0xFF

        # Finally write the card.
        util.rewrite(4, data)
        print('Wrote card successfully! You may now remove the card from the RC522.')
        run = False
