#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Adafruit_LED_Backpack import SevenSegment
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import time

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)
# Initialize the segment
segment = SevenSegment.SevenSegment(address=0x70)
segment.begin()

tonePin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(tonePin, GPIO.IN)
GPIO.setup(tonePin, GPIO.OUT)
p = GPIO.PWM(tonePin, 100)

# setup the LCD for merry xmas
lcd.set_backlight(0)
lcd.message('Merry Christmas \n from Elecrow!')
# set the segment 12:25 (December 25th)
segment.set_digit(0, 1)
segment.set_digit(1, 2)
segment.set_digit(2, 2)
segment.set_digit(3, 5)
# Toggle colon at 1Hz
segment.set_colon(1 % 2)
segment.write_display()

# High-level abstraction of the Arduino's Delay function
def delay(times):
    time.sleep(times/500.0)

# High-level abstraction of the Arduino's Tone function, though this version is blocking
def tone(pin, pitch, duration):
    if pitch == 0:
        delay(duration)
        return
    p = GPIO.PWM(tonePin, pitch)

    # Change the duty-cycle to 50 if you wish
    p.start(30)
    delay(duration)
    p.stop()

    # Delay used to discourage overlap of PWM cycles
    delay(2)

def midi():
    try:
        tone(tonePin, 261, 173.25)
        delay(20.8333333333)
        tone(tonePin, 349, 173.25)
        delay(20.8333333333)
        tone(tonePin, 349, 87.0)
        delay(10.0)
        tone(tonePin, 391, 87.0)
        delay(10.0)
        tone(tonePin, 349, 87.0)
        delay(10.0)
        tone(tonePin, 220, 58.5)
        tone(tonePin, 329, 28.5)
        delay(10.0)
        tone(tonePin, 293, 173.25)
        delay(20.8333333333)
        tone(tonePin, 293, 173.25)
        delay(20.8333333333)
        tone(tonePin, 174, 154.5)
        tone(tonePin, 293, 18.75)
        delay(20.8333333333)
        tone(tonePin, 391, 173.25)
        delay(20.8333333333)
        tone(tonePin, 391, 87.0)
        delay(10.0)
        tone(tonePin, 440, 87.0)
        delay(10.0)
        tone(tonePin, 391, 87.0)
        delay(10.0)
        tone(tonePin, 195, 58.5)
        tone(tonePin, 349, 28.5)
        delay(10.0)
        tone(tonePin, 329, 173.25)
        delay(20.8333333333)
        tone(tonePin, 329, 173.25)
        delay(20.8333333333)
        tone(tonePin, 261, 154.5)
        tone(tonePin, 329, 18.75)
        delay(20.8333333333)
        tone(tonePin, 440, 173.25)
        delay(20.8333333333)
        tone(tonePin, 440, 87.0)
        delay(10.0)
        tone(tonePin, 466, 87.0)
        delay(10.0)
        tone(tonePin, 440, 87.0)
        delay(10.0)
        tone(tonePin, 277, 58.5)
        tone(tonePin, 391, 28.5)
        delay(10.0)
        tone(tonePin, 349, 173.25)
        delay(20.8333333333)
        tone(tonePin, 293, 173.25)
        delay(20.8333333333)
        tone(tonePin, 261, 87.0)
        delay(10.0)
        tone(tonePin, 261, 87.0)
        delay(10.0)
        tone(tonePin, 293, 173.25)
        delay(20.8333333333)
        tone(tonePin, 233, 154.5)
        tone(tonePin, 391, 18.75)
        delay(20.8333333333)
        tone(tonePin, 329, 173.25)
        delay(20.8333333333)
        tone(tonePin, 349, 346.5)
        delay(41.6666666667)
        tone(tonePin, 261, 173.25)
        delay(20.8333333333)
        tone(tonePin, 349, 173.25)
        delay(20.8333333333)
        tone(tonePin, 349, 173.25)
        delay(20.8333333333)
        tone(tonePin, 174, 154.5)
        tone(tonePin, 349, 18.75)
        delay(20.8333333333)
        tone(tonePin, 329, 346.5)
        delay(41.6666666667)
        tone(tonePin, 233, 154.5)
        tone(tonePin, 329, 18.75)
        delay(20.8333333333)
        tone(tonePin, 349, 173.25)
        delay(20.8333333333)
        tone(tonePin, 329, 173.25)
        delay(20.8333333333)
        tone(tonePin, 195, 154.5)
        tone(tonePin, 293, 18.75)
        delay(20.8333333333)
        tone(tonePin, 261, 346.5)
        delay(41.6666666667)
        tone(tonePin, 391, 173.25)
        delay(20.8333333333)
        tone(tonePin, 440, 173.25)
        delay(20.8333333333)
        tone(tonePin, 391, 87.0)
        delay(10.0)
        tone(tonePin, 391, 87.0)
        delay(10.0)
        tone(tonePin, 349, 87.0)
        delay(10.0)
        tone(tonePin, 220, 58.5)
        tone(tonePin, 349, 28.5)
        delay(10.0)
        tone(tonePin, 523, 173.25)
        delay(20.8333333333)
        tone(tonePin, 261, 173.25)
        delay(20.8333333333)
        tone(tonePin, 261, 87.0)
        delay(10.0)
        tone(tonePin, 174, 58.5)
        tone(tonePin, 261, 28.5)
        delay(10.0)
        tone(tonePin, 293, 173.25)
        delay(20.8333333333)
        tone(tonePin, 195, 154.5)
        tone(tonePin, 391, 18.75)
        delay(20.8333333333)
        tone(tonePin, 329, 173.25)
        delay(20.8333333333)
        tone(tonePin, 349, 346.5)
    except KeyboardInterrupt:
        # Turn the screen off
        lcd.clear()
        lcd.set_backlight(1)
        # clean the segment
        segment.clear()
        segment.write_display()
        # clean GPIO pins
        GPIO.cleanup()
        exit()


while True:
    midi()
