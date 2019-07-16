#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import time
import RPi.GPIO as GPIO

# define LED pin
led_pin = 26

# set GPIO mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)
# set puin as input
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # turn on LED
        GPIO.output(led_pin, GPIO.HIGH)
        # Wait half a second
        time.sleep(0.2)
        # turn off LED
        GPIO.output(led_pin, GPIO.LOW)
        # Wait half a second
        time.sleep(0.2)
except KeyboardInterrupt:
    # CTRL+C detected, cleaning and quitting the script
    GPIO.cleanup()
