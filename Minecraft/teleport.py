#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from mcpi.minecraft import Minecraft
import time

# create Minecraft Object
mc = Minecraft.create()

# set touch pin
touch_pin = 11
# set gpio mode as GPIO BOARD
GPIO.setmode(GPIO.BOARD)
# set as INPUT
GPIO.setup(touch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(touch_pin) == True: # look for button press
        mc.player.setPos(0, 0, 0) # teleport player
        print("Teleported successfully!")
        time.sleep(0.5) # wait 0.5 seconds
