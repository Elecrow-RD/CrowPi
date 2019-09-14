# Copyright 2019, Tozny LLC

import sys
import json
import e3db
import argparse
from e3db.types import Search

config = e3db.Config.load('json-test-client')
client = e3db.Client (config)


def isJsonStdioCLI ():
    if '--json-stdio' in sys.argv:
        return True

def isToznyCLI ():
    if '--tozny' in sys.argv:
        return True
    
def getStdIn ():
    s = sys.stdin.read()
    return (json.loads(s))


def putStdIo(m):
    print (json.dumps (m))
    if isToznyCLI:
        client.write(m["sensor-type"], m)

def toznyTypeCLI():
    for arg in sys.argv:
        if '--tozny-type=' in arg:
            return (arg.split("=")[1])
        
def readTozny(sensorType, displayAndWait):
    query = Search(include_data=True).match(record_types=[sensorType])
    print ("runing query")
    results = client.search(query)
    print ("finished query")
    for record in results:
        displayAndWait(record.data["message"], int(record.data["period-ms"]))
        print (record.data)
    
def fetchAndDisplaySensors(displayAndWait):
    sensorType = toznyTypeCLI()
    if (sensorType != None):
        readTozny(sensorType, displayAndWait)
    exit()
