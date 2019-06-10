from mcpi.minecraft import Minecraft
import RPi.GPIO as GPIO
import time

# store the GPIO control pins
UP_PIN = 37
DOWN_PIN = 33
LEFT_PIN = 22
RIGHT_PIN = 35

# set GPIO mode to GPIO BOARD
GPIO.setmode(GPIO.BOARD)

# set gpio buttons as INPUT
GPIO.setup(UP_PIN, GPIO.IN)
GPIO.setup(DOWN_PIN, GPIO.IN)
GPIO.setup(LEFT_PIN, GPIO.IN)
GPIO.setup(RIGHT_PIN, GPIO.IN)

# create Minecraft Object
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    if(GPIO.input(UP_PIN) == 0):
        mc.player.setPos(x-0.1, y, z+0.1)
        print "Moving up ...")
    if(GPIO.input(DOWN_PIN) == 0):
        mc.player.setPos(x+0.1, y, z-0.1)
        print("Moving down ...")
    if(GPIO.input(LEFT_PIN) == 0):
        print("Moving left ...")
    if(GPIO.input(RIGHT_PIN) == 0):
        print("Moving right ...")
