#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# define motion pin
motion_pin = 23

# set GPIO as GPIO.BOARD
GPIO.setmode(GPIO.BCM)
# set pin mode as INPUT
GPIO.setup(motion_pin, GPIO.IN)

try:
    while True:
       if(GPIO.input(motion_pin) == 0):
             print("Nothing moves ...")
       elif(GPIO.input(motion_pin) == 1):
             print("Motion detected!")
       time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
