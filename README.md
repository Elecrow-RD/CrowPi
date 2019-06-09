# CrowPi

Official Elecrow CrowPi Repository

# Preperation

We will need some dependencies to be installed on a clean image in order for everything to work.
make sure to install those dependencies on your raspberry pi if you are not using our already-made image.

````
sudo apt-get update
sudo apt-get install build-essential python-dev python3-dev python-smbus python3-smbus python-pip python3-pip python-pil python3-pil
````

Make sure you have the RPi.GPIO library by executing:

````
sudo pip install RPi.GPIO
````

Then run the command ```` sudo raspi-config ```` and under "interface options" make sure to enable SPI and I2C
also expand the filesystem if you haven't done it already in the advanced options.

# Drivers installation

In case you are not using a pre-built CrowPi image and want to install everything by yourself, there are several steps you need to take
First, you need to clone the entire repository to your CrowPi desktop by the Following commands
````
git clone https://github.com/Elecrow-keen/CrowPi.git
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
sudo python setup.py install
sudo python3 setup.py install
cd ..
````
Adafruit_Python_DHT:
````
cd Adafruit_Python_DHT
sudo python setup.py install
sudo python3 setup.py install
cd ..
````
Adafruit_Python_LED_Backpack:
````
cd Adafruit_Python_LED_Backpack
sudo python setup.py install
sudo python3 setup.py install
cd ..
````
Luma Matrix LED:
````
cd luma.led_matrix
sudo python setup.py install
sudo python3 setup.py install
cd ..
````

Afterwards you should have all the drivers ready both for Python2 and Python3.

# Setting up IR Receiver

The IR Receiver requires some extra installations to work
First, install the LIRC library:
````
sudo apt-get install lirc
sudo apt-get install python-lirc python3-lirc
````
After installing the following libraries, inside CrowPi/Drivers/LIRC folder that we cloned, there are 3 files
you need to copy the files to the LIRC configuration directory:
````
/etc/lirc
````

After you moved the configuration file, edit your boot config file ````sudo nano /boot/config.txt````
and where it says
````
# Uncomment this to enable the lirc-rpi module
#dtoverlay=lirc-rpi
````
change it to this
````
# Uncomment this to enable the lirc-rpi module
dtoverlay=lirc-rpi,gpio_in_pin=20
````

The last part would be to edit the modules configuration file
````
sudo nano /etc/modules
````
and add the following lines inside
````
lirc_dev
lirc_rpi gpio_in_pin=20
````
