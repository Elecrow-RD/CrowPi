# Copyright 2019, Tozny LLC

import sys
import json

def isJsonStdioCLI ():
    if '--json-stdio' in sys.argv:
        return True

def getStdIn ():
    s = sys.stdin.read()
    return (json.loads(s))


def putStdIo(m):
    print (json.dumps (m))
