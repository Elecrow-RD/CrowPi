#!/usr/bin/python

import jsonstdio as J

ex = {
    "json-stdio":True,
    "sensor-type":"ultrasonic",
    "message":"3, 4, 5",
    "period-ms":1000,
    "x":3,
    "y":4,
    "z":5
}

if J.isJsonStdioCLI():
    J.putStdIo (ex)
