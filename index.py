#!/usr/bin/python3

# https://exchangeratesapi.io/

import http.client
import json
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

args = sys.argv[1]
splitInput = args.split(" ")

if len(splitInput) > 3:
    amount = float(splitInput[0])
    fromC = splitInput[1].upper()
    toC = splitInput[3].upper()

    conn = http.client.HTTPSConnection("api.exchangeratesapi.io")

    conn.request("GET", f'/latest?base={fromC}&symbols={toC}')

    r1 = conn.getresponse()
    data1 = r1.read()
    jsonData = json.loads(data1)

    oneOfTarget = jsonData["rates"][toC]

    convertedAmount = oneOfTarget*amount

    result = {
            "items": [
                {
                    "title": convertedAmount,
                    "subtitle": toC,
                    "arg": convertedAmount,
                    "icon": {
                        "path": "cicon.png"
                    }
                }
            ]
        }
    alfredOutput = json.dumps(result)

    print(alfredOutput)

else:
    result = {
            "items": [
                {
                    "title": "Waiting to finish request...",
                    "icon": {
                        "path": "cicon.png"
                    }
                }
            ]
        }
    alfredOutput = json.dumps(result)

    print(alfredOutput)