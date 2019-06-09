#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# define vibration pin
vibration_pin = 13

# Set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BOARD)

# Setup vibration pin to OUTPUT
GPIO.setup(vibration_pin, GPIO.OUT)

# turn on vibration
GPIO.output(vibration_pin, GPIO.HIGH)
# wait half a second
time.sleep(0.5)
# turn off vibration
GPIO.output(vibration_pin, GPIO.LOW)
# cleaup GPIO
GPIO.cleanup()
