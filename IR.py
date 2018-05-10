import socket, signal
import lirc, time, sys
import RPi.GPIO as GPIO
from  array import array

GPIO.setmode(11)
GPIO.setup(17, 0)
GPIO.setup(18, 0)
PORT = 42001
HOST = "localhost"
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Lirc = lirc.init("keys")
#lirc.set_blocking(False, Lirc)		# Un-Comment to stop nextcode() from waiting for a signal ( will return empty array when no key is pressed )

def handler(signal, frame):
	Socket.close()
	GPIO.cleanup()
	exit(0)

signal.signal(signal.SIGTSTP, handler)

def sendCmd(cmd):
    n = len(cmd)
    a = array('c')
    a.append(chr((n >> 24) & 0xFF))
    a.append(chr((n >> 16) & 0xFF))
    a.append(chr((n >> 8) & 0xFF))
    a.append(chr(n & 0xFF))
    Socket.send(a.tostring() + cmd)

while True:

	Out = lirc.nextcode()
	print Out[0]
