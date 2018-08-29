import RPi.GPIO as GPIO
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create() # create Minecraft Object

buzzer_pin = 12 # store the GPIO pin number

GPIO.setmode(GPIO.BOARD) # change GPIO mode to BOARD
GPIO.setup(buzzer_pin, GPIO.OUT) # setup the pin to OUTPUT

# repeat indefinitely
while True:
    # get player position
    x, y, z = mc.player.getPos()
    # look at every block until block 15
    for i in range(15):
        if mc.getBlock(x, y - i, z) == 46:
            GPIO.output(buzzer_pin, True) # buzz the buzzer on
            time.sleep(0.5) # wait
            GPIO.output(buzzer_pin, False) # turn the buzzer off
            time.sleep(0.5) # wait
