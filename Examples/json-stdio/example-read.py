#!/usr/bin/python

import jsonstdio as J
import json

if J.isJsonStdioCLI():
    d = J.getStdIn()
    oldMsg = d["message"]
    d["message"] = oldMsg + " YEAH"
    print json.dumps(d)

