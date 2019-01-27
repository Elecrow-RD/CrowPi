# Python RC522 library

pi-rc522 consists of two Python classes for controlling an SPI RFID module "RC522" using Raspberry Pi or Beaglebone Black. You can get this module on AliExpress or eBay for $3.

Based on [MFRC522-python](https://github.com/mxgxw/MFRC522-python/blob/master/README.md).
Original library link https://github.com/ondryaso/pi-rc522.git
all rights reserved to @ondryaso this library been modified to work with the CrowPi.

get source code:
```
git clone https://github.com/elecrow-keen/CrowPi.git
cd CrowPi/Drivers/RFID/
python setup.py install
```

You'll also need to install the [**spidev**](https://pypi.python.org/pypi/spidev) and [**RPi.GPIO**](https://pypi.python.org/pypi/RPi.GPIO) libraries on Raspberry PI, and [**Adafruit_BBIO**](https://github.com/adafruit/adafruit-beaglebone-io-python) on Beaglebone Black (which should be installed by default).

[MIFARE datasheet](https://www.nxp.com/docs/en/data-sheet/MF1S50YYX_V1.pdf) can be useful.
