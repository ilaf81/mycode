#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import urllib.request
import json
import requests


## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
        
    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    ## put fileobject into helmet
    helmet = groundctrl.read()
    
    ## decode JSON to Python data structure
    helmetson = json.loads(helmet.decode('utf-8'))
    
    ## display our Pythonic data
    #print("\n\nConverted Python data")
    #print(helmetson)
    
    print('\n\nPeople in Space: ', helmetson["number"])
    for astronaut in helmetson["people"]:
        #print(astronaut)
        print(f'{astronaut["name"]} on the {astronaut["craft"]}')
    #people = helmetson['people']
    #print(people)
    
main()



#Challenge 2

## Define URL
req_M = requests.get("http://api.open-notify.org/astros.json")

def req_main():

    ## Call the webservice
    #groundctrl = urllib.request.urlopen(MAJORTOM)

    ## put fileobject into helmet
   # helmet = groundctrl.read()

    ## decode JSON to Python data structure
    helmetson = req_M.json()

    ## display our Pythonic data
    #print("\n\nConverted Python data")
    #print(helmetson)

    print('\n\nPeople in Space: ', helmetson["number"])
    for astronaut in helmetson["people"]:
        #print(astronaut)
        print(f'{astronaut["name"]} on the {astronaut["craft"]}')
    #people = helmetson['people']
    #print(people)

req_main()
