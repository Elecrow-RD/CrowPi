# CrowPi

Official Elecrow CrowPi Repository

# What's new?

Now Raspberry Pi 4 is officially supported, both for python3 and python2 scripts.
There is some issue with LIRC Python3 library (IR sensor) if you are running Raspbian Buster release (Latest), We are working to fix it ASAP.

# Preparation

We will need some dependencies to be installed on a clean image in order for everything to work.
make sure to install those dependencies on your raspberry pi if you are not using our already-made image.

````
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential python-dev python3-dev python-smbus python3-smbus python-pip python3-pip python-pil python3-pil liblircclient-dev
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
RC-522 RFID:
````
cd RFID/SPI-Py
sudo python setup.py install
sudo python3 setup.py install
cd ..
````

Afterwards you should have all the drivers ready both for Python2 and Python3.

# Setting up IR Receiver

The IR Receiver requires some extra installations to work.

First, Install the LIRC library and the python driver to support our custom python script
````
sudo apt-get install lirc
````
If it gives you errors, don't worry. It will be fixed later.

Now run:
````
sudo pip install python-lirc
sudo pip3 install python-lirc
````
Note: on the latest Raspbian pip3 install python-lirc will not work, we are working to solve it ASAP.

Inside CrowPi/Drivers/LIRC folder that we cloned, there are 3 files
you need to copy the files to the LIRC configuration directory, from the CrowPi folder run the following commands:
````
sudo cp Drivers/LIRC/* /etc/lirc
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
dtoverlay=gpio-ir,gpio_pin=20
````
previously it used to be ````dtoverlay=lirc-rpi```` but this one got deprecated in the newer version of Raspbian.

Execute the following commands to copy the configuration files
````
sudo cp /etc/lirc/lirc_options.conf.dist /etc/lirc/lirc_options.conf
sudo cp /etc/lirc/lircd.conf.dist /etc/lirc/lircd.conf
````

edit ````/etc/lirc/lirc_options.conf```` by writing the command ````sudo nano /etc/lirc/lirc_options.conf````
and modify the following lines to be exact as here:
````
driver = default
device = /dev/lirc0
````

now reboot
````
sudo reboot
````

Now run apt-get install Lirc once again to fix the previous errors if any
````
sudo apt-get install lirc
````

Last step, stop the LIRC library so we could use the IR driver with our python script
````
sudo /etc/init.d/lirc stop
````
Note: if you get runtime error that the command cannot be found, maybe you have a different version of LIRC, try this command instead:
````
sudo /etc/init.d/lircd stop
````
