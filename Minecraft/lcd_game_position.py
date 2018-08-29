#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import Adafruit_CharLCD as LCD
from mcpi.minecraft import Minecraft

# Define Minecraft

mc = Minecraft.create()

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

# Turn LCD backlight on
lcd.set_backlight(0)

while True:
	# get player position
	x, y, z = mc.player.getPos()
	x, y, z = float(str(x)[:3]),float(str(y)[:3]),float(str(z)[:3])
	pos = str(x)+", "+str(y)+", "+str(z)
	print pos
	lcd.message('Position:\n%s' % pos)
	time.sleep(1)
	lcd.clear()
	#time.sleep(0.5)
