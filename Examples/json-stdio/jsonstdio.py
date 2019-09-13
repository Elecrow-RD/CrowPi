# Copyright 2019, Tozny LLC

import sys
import json
import e3db

config = e3db.Config.load('json-test-client')
client = e3db.Client (config)


def isJsonStdioCLI ():
    if ('--json-stdio' in sys.argv
        or '--tozny' in sys.argv):
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

