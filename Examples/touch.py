#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# define touch pin
touch_pin = 17

# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# set GPIO pin to INPUT
GPIO.setup(touch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # check if touch detected
        if(GPIO.input(touch_pin)):
            print('Touch Detected')
        time.sleep(0.1)
except KeyboardInterrupt:
    # CTRL+C detected, cleaning and quitting the script
    GPIO.cleanup()
