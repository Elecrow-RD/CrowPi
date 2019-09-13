#!/usr/bin/python

import time
import datetime
from Adafruit_LED_Backpack import SevenSegment

import sys
sys.path.insert (1, './json-stdio')
import jsonstdio as J

# ===========================================================================
# Clock Example
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

if J.isJsonStdioCLI():
  d = J.getStdIn()
  segment.clear()
  message = 123.4
  if (d["sensor-type"] == "ultrasonic"):
    message = float(d["distance"])
  segment.print_float(message, decimal_digits=1, justify_right=True)
  segment.write_display()
  time.sleep (int(d["period-ms"]) / 1000)
  segment.clear()
  segment.write_display()
  exit()
      
print("Press CTRL+Z to exit")

# Continually update the time on a 4 char, 7-segment display
try:
  while(True):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    segment.clear()
    # Set hours
    segment.set_digit(0, int(hour / 10))     # Tens
    segment.set_digit(1, hour % 10)          # Ones
    # Set minutes
    segment.set_digit(2, int(minute / 10))   # Tens
    segment.set_digit(3, minute % 10)        # Ones
    # Toggle colon
    segment.set_colon(second % 2)              # Toggle colon at 1Hz

    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    segment.write_display()

    # Wait a quarter second (less than 1 second to prevent colon blinking getting$
    time.sleep(0.25)
except KeyboardInterrupt:
    segment.clear()
    segment.write_display()
