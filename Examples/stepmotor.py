#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : Original author ludwigschuster
# Original Author Github: https://github.com/ludwigschuster/RasPi-GPIO-Stepmotor
# http://elecrow.com/

import time
import RPi.GPIO as GPIO
import math

class Stepmotor:

	def __init__(self):

		# set GPIO mode
		GPIO.setmode(GPIO.BOARD)
		# These are the pins which will be used on the Raspberry Pi
		self.pin_A = 29
		self.pin_B = 31
		self.pin_C = 33
		self.pin_D = 35
		self.interval = 0.010

		# Declare pins as output
		GPIO.setup(self.pin_A,GPIO.OUT)
		GPIO.setup(self.pin_B,GPIO.OUT)
		GPIO.setup(self.pin_C,GPIO.OUT)
		GPIO.setup(self.pin_D,GPIO.OUT)
		GPIO.output(self.pin_A, False)
		GPIO.output(self.pin_B, False)
		GPIO.output(self.pin_C, False)
		GPIO.output(self.pin_D, False)

	def Step1(self):

		GPIO.output(self.pin_D, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_D, False)

	def Step2(self):

		GPIO.output(self.pin_D, True)
		GPIO.output(self.pin_C, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_D, False)
		GPIO.output(self.pin_C, False)

	def Step3(self):

		GPIO.output(self.pin_C, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_C, False)

	def Step4(self):

		GPIO.output(self.pin_B, True)
		GPIO.output(self.pin_C, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_B, False)
		GPIO.output(self.pin_C, False)

	def Step5(self):

		GPIO.output(self.pin_B, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_B, False)

	def Step6(self):

		GPIO.output(self.pin_A, True)
		GPIO.output(self.pin_B, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_A, False)
		GPIO.output(self.pin_B, False)

	def Step7(self):

		GPIO.output(self.pin_A, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_A, False)

	def Step8(self):

		GPIO.output(self.pin_D, True)
		GPIO.output(self.pin_A, True)
		time.sleep(self.interval)
		GPIO.output(self.pin_D, False)
		GPIO.output(self.pin_A, False)

	def turn(self,count):
		for i in range (int(count)):
			self.Step1()
			self.Step2()
			self.Step3()
			self.Step4()
			self.Step5()
			self.Step6()
			self.Step7()
			self.Step8()

	def close(self):
		# cleanup the GPIO pin use
		GPIO.cleanup()

	def turnSteps(self, count):
		# Turn n steps
		# (supply with number of steps to turn)
		for i in range (count):
			self.turn(1)

	def turnDegrees(self, count):
		# Turn n degrees (small values can lead to inaccuracy)
		# (supply with degrees to turn)
		self.turn(round(count*512/360,0))

	def turnDistance(self, dist, rad):
		# Turn for translation of wheels or coil (inaccuracies involved e.g. due to thickness of rope)
		# (supply with distance to move and radius in same metric)
		self.turn(round(512*dist/(2*math.pi*rad),0))

def main():

	print("moving started")
	motor = Stepmotor()
	print("One Step")
	motor.turnSteps(1)
	time.sleep(0.5)
	print("20 Steps")
	motor.turnSteps(20)
	time.sleep(0.5)
	print("quarter turn")
	motor.turnDegrees(90)
	print("moving stopped")
	motor.close()

if __name__ == "__main__":
    main()
