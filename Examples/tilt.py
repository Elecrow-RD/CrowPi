#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import time
import RPi.GPIO as GPIO

# define tilt pin
tilt_pin = 22

# set GPIO mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)
# set puin as input
GPIO.setup(tilt_pin, GPIO.IN)

try:
    while True:
        # positive is tilt to left negative is tilt to right
        if GPIO.input(tilt_pin):
            print("[-] Left Tilt")
        else:
            print("[-] Right Tilt")
        time.sleep(1)
except KeyboardInterrupt:
    # CTRL+C detected, cleaning and quitting the script
    GPIO.cleanup()
