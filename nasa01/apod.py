#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard libray
# import webbrowser

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=psW2K4duM09Q9GD8aHleBcW3CWVCua759xP7JoO0' ## this is our api key
print("Please enter the date(yyyy-mm-dd) you would like to check. Or press Enter")
date = input()
NASAAPI = NASAAPI + "date=" + date + "&"


print("Would you like HD picture(yes/no)")
hd_response = input().lower()
if hd_response == "yes":
    NASAAPI = NASAAPI + "hd=True&"
else:
    NASAAPI = NASAAPI + "hd=False&"

## pretty print json
def main():
    """run-time code"""
    nasaapiobj = requests.get(NASAAPI + MYKEY) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json
    print(nasaread) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread['explanation']) # display the value for the key explanation
    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))

    print(NASAAPI + MYKEY)
   # input('\nPress ENTER to view this photo of the day') # pause for ENTER
   # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

main()

