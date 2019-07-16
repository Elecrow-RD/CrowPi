#!/usr/bin/env python
# -*- coding: utf8 -*-
# Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True
# Incase user wants to terminate, this function is exactly for that reason.
def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)
# create the reader object
MIFAREReader = MFRC522.MFRC522()

# Welcome greeting
print("Welcome to MFRC522 RFID Read example")
print("Press CTRL+C anytime to quit.")

# The function will continue running to detect untill user said otherwise
while continue_reading:
    # detect touch of the card, get status and tag type
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    # check if card detected or not
    if status == MIFAREReader.MI_OK:
        print("Card detected")

    # Get the RFID card uid and status
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If status is alright, continue to the next stage
    if status == MIFAREReader.MI_OK:
        # Print UID
        print("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
        # standard key for rfid tags
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
        # authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
        # check if authenticated successfully, read the data
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print("Authentication error")
