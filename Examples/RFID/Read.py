#!/usr/bin/env python
# -*- coding: utf8 -*-
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
import RPi.GPIO as GPIO
import MFRC522
import signal
continue_reading = True
# Funktion um cleanup Funktionen durchzuführen wenn das Script abgebrochen wird.
def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)
# Erstelle ein objekt aus der Klasse MFRC522
MIFAREReader = MFRC522.MFRC522()

# Wilkommensnachricht
print("Willkommen beim MFRC522 Lese Beispiel.")
print("Druecke STRG+C zum Beenden.")

# Diese Schleife Sucht dauerhaft nach Chips oder Karten. Wenn eine nah ist bezieht er die UID und identifiziert sich.
while continue_reading:
    # Nach Chips und Karten scannen    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    # Wenn eine Karte gefunden wurde
    if status == MIFAREReader.MI_OK:
        print("Card detected")
    
    # Beziehe UID der Karte
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # Wenn UID vorhanden fortfahren
    if status == MIFAREReader.MI_OK:
        # Print UID
        print("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))    
        # Standard Schlüssel für Authentifizierungen
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]   
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
        # Authentifizieren
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
        # Prüfen ob authentifiziert
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print("Authentication error")
