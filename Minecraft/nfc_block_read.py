# Raspberry Pi Minecraft Block NFC Listener
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

import binascii
import socket
import time
import signal
import sys
from pirc522 import RFID
import mcpi.minecraft as minecraft
import minecraft_blocks

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

# Number of seconds to delay after building a block.  Good for slowing down the
# update rate to prevent flooding new blocks into the world.
MAX_UPDATE_SEC = 0.5


def create_block(mc, block_id, subtype=None):
    """Build a block with the specified id and subtype under the player in the
    Minecraft world.  Subtype is optional and can be specified as None to use
    the default subtype for the block.
    """
    # Get player tile position and real position.
    ptx, pty, ptz = mc.player.getTilePos()
    px, py, pz = mc.player.getPos()
    # Create block at current player tile location.
    if subtype is None:
        mc.setBlock(ptx, pty, ptz, block_id)
    else:
        mc.setBlock(ptx, pty, ptz, block_id, subtype)
    # Move the player's real positon up one block.
    mc.player.setPos(px, py+1, pz)


# Start with no connection to the Minecraft world, instead it will be created
# as soon as a block is swiped.
mc = None

print('Minecraft Block NFC Listener')
print('')
print('Waiting for NFC card...')

while run:
    rdr.wait_for_tag()
    (error, data) = rdr.request()
    if not error:
        print("[-] Card Detected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        # Found a card, now try to read block 4 to detect the block type.
        print("[-] Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
        # First authenticate block 4.
        util.set_tag(uid)
        # set authorization key
        util.auth(rdr.auth_b, CARD_KEY)
        # read the data from the card
        util.read_out(4)
        (error, data) = rdr.read(4)

        if data is None:
            print('Failed to read data from card!')
            continue

        # Check if card has Minecraft block data by looking for header 'MCPI'
        if data[0:4] != [77, 67, 80, 73]:
            print('Card is not written with Minecraft block data!')
            continue
        # Parse out the block type and subtype.
        block_id = data[4]
        has_subtype = data[5]
        subtype_id = data[6]
        # Find the block name (it's ugly to search for it, but there are less than 100).
        for block in minecraft_blocks.BLOCKS:
            if block[1] == block_id:
                block_name = block[0]
                break

        print('Found block!')
        print('Type: {0}'.format(block_name))

        if has_subtype:
            subtype_name = minecraft_blocks.SUBTYPES[block_name][subtype_id]
            print('Subtype: {0}'.format(subtype_name))

        # Try to create the block in Minecraft.
        # First check if connected to Minecraft world.

        try:
            if mc is None:
                mc = minecraft.Minecraft.create()
            create_block(mc, block_id, subtype_id if has_subtype else None)
            time.sleep(MAX_UPDATE_SEC)
        except socket.error:
            # Socket error, Minecraft probably isn't running.
            print('Could not connect to Minecraft, is the game running in a world?')
            time.sleep(1)
            continue
