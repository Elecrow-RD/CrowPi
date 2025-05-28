### Product Links：https://www.elecrow.com/crowpi-compact-raspberry-pi-educational-kit.html

# CrowPi

Official Elecrow CrowPi Repository

# What's new?

Update Dec 11th: it's seems some packages are getting damaged in python2 due to the unsupported python version. Now we (and everyone else) will only support python3. no python2 support will be given.

# Preparation

We will need some dependencies to be installed on a clean image in order for everything to work.
make sure to install those dependencies on your raspberry pi if you are not using our already-made image.

````
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential python3-dev python3-smbus python3-pip python3-pil liblircclient-dev
````

Make sure you have the RPi.GPIO library by executing:

````
sudo pip install RPi.GPIO
sudo pip3 install RPi.GPIO
````

Then run the command ```` sudo raspi-config ```` and under "interface options" make sure to enable SPI and I2C
also expand the filesystem if you haven't done it already in the advanced options.

# Drivers installation

In case you are not using a pre-built CrowPi image and want to install everything by yourself, there are several steps you need to take
First, you need to clone the entire repository to your CrowPi desktop by the Following commands
````
git clone https://github.com/Elecrow-RD/CrowPi.git
cd CrowPi/Drivers
````
Now when we are inside the driver directory, there are several drivers you need to know about:

* Adafruit_Python_CharLCD - Library to control the LCD screen on the CrowPi
* Adafruit_Python_DHT - Library to control the DH11 Sensor (temperature and humidity)
* Adafruit_Python_LED_Backpack - Library to control the segment LED
* luma.led_matrix - Library to control the Matrix LED
* RFID - Library to control the NFC RC-522 NFC reader/writer

You will need to install each of those drivers by running the following command for each one:
Adafruit_Python_CharLCD:
````
cd Adafruit_Python_CharLCD
sudo python3 setup.py install
cd ..
````
Adafruit_Python_DHT:
````
cd Adafruit_Python_DHT
sudo python3 setup.py install
cd ..
````
Adafruit_Python_LED_Backpack:
````
cd Adafruit_Python_LED_Backpack
sudo python3 setup.py install
cd ..
````
Luma Matrix LED:
````
cd luma.led_matrix
sudo python3 setup.py install
cd ..
````
RC-522 RFID:
````
cd RFID/SPI-Py
sudo python3 setup.py install
cd ..
````

Afterwards you should have all the drivers ready, head to the example folder to run example and test it for yourself.
