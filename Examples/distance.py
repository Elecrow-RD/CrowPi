#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : www.modmypi.com
# Link: https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

import RPi.GPIO as GPIO
import time
import sys

sys.path.insert (1, './json-stdio')
import jsonstdio as J

GPIO.setmode(GPIO.BCM)

TRIG = 16
ECHO = 12

if not J.isJsonStdioCLI():
  print("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
if not J.isJsonStdioCLI():
  print("Waiting For Sensor To Settle")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

if J.isJsonStdioCLI():
  d = {
    "json-stdio":True,
    "sensor-type":"ultrasonic",
    "message":"Distance: " + str (distance),
    "distance":distance,
    "period-ms":1000
    }
  J.putStdIo(d)
else:
  print("Distance: %scm" % distance)

GPIO.cleanup()
