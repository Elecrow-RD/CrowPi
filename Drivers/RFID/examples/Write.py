#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#
import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

# Funktion um cleanup Funktionen durchzuführen wenn das Script abgebrochen wird.
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)

# Erstelle ein Objekt aus der Klasse MFRC522
MIFAREReader = MFRC522.MFRC522()

# Diese Schleife Sucht dauerhaft nach Chips oder Karten. Wenn eine nah ist bezieht er die UID und identifiziert sich.
while continue_reading:

    # SUcht Karten
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Wenn Karte gefunden
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # UID der Karte erhalten
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # Wenn UID erhalten, fortfahren
    if status == MIFAREReader.MI_OK:

        # UID in Konsole ausgeben
        print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])

        # Standard Schlüssel für Authentifizierungen
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]


        MIFAREReader.MFRC522_SelectTag(uid)

        # Authentifizieren
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
        print "\n"

        # Prüfen ob authentifiziert
        if status == MIFAREReader.MI_OK:

            # Variablen der Werte die auf der Karte gespeichert werden sollen.
            data = [99, 11, 55, 66, 44, 111, 222, 210, 125, 153, 136, 199, 144, 177, 166, 188]

            for x in range(0,16):
                data.append(0xFF)

            print "Sector 8 looked like this:"
            # Block 8 lesen
            MIFAREReader.MFRC522_Read(8)
            print "\n"

            print "Sector 8 will now be filled with 0xFF:"
            # Dateien Schreiben
            MIFAREReader.MFRC522_Write(8, data)
            print "\n"

            print "It now looks like this:"
            # Überprüfen ob beschrieben wurde
            MIFAREReader.MFRC522_Read(8)
            print "\n"

            MIFAREReader.MFRC522_StopCrypto1()

            # Sicherstellen das, das Kartenlesen eingestellt wird.
            continue_reading = False
        else:
            print "Authentification error"
