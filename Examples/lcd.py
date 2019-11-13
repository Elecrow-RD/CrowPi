#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import Adafruit_CharLCD as LCD
import Adafruit_DHT

# set type of DHsensor
sensor = 11
# set pin number
dh11_pin = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

try:
    while True:
    # Turn backlight on
    lcd.set_backlight(0)
    # get temperature and humidity
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # clean the LCD screen
    lcd.clear()
    # Un-comment the line below to convert the temperature to Fahrenheit.
    # temperature = temperature * 9/5.0 + 32
    if humidity is not None and temperature is not None:
        lcd.message('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading, Retrying in 5 seconds!')
    # wait 5 seconds for the next try
    time.sleep(5)
except KeyboardInterrupt:
    # Turn the screen off
    lcd.clear()
    lcd.set_backlight(1)
