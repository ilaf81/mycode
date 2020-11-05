#!/usr/bin/env python3
import time
import requests ## 3rd party URL lookup

# CODE CUSTOMIZATION 02 - Create a function that expects a parameter of the missdistance in miles and
# returns the number of 'moon lengths' away that body is. A 'moon length' = 238,900 miles. Use this new 
# function to display this additional data to the user.

lunar_dist = 0.0
dist_miles = 0.0
end_date = ""

def lunar_distance(miles):
    l_distance = miles / 238900
    return l_distance

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2018-06-01'  ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=sT45viTJl59kKEMAdqu9qelVFxi3ohH3KhXbF29V' ## replace this with our API key

    print("Would like a specific end-date? (yes/no)")
    ans = input().lower()
    if ans == "yes":
        print("Please enter the date(YYYY-MM-DD)")
        end_date = input()
        #print(end_date)
        enddate ='&end_date='+ end_date
        #print(enddate)
        time.sleep(3)
        neourl = neourl + startdate + enddate + mykey
    else:
        neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json() 
    print(neourl) 
    dates= []
    for DATE in neojson["near_earth_objects"]:
        dates.append(DATE)
    
    for date in dates:
        print("\n\n" + date)
        #print(neourl)
        time.sleep(2)
        for x in neojson["near_earth_objects"][date]:
            if x["name"]:
                print(x["name"])
                dist_miles = float( neojson["near_earth_objects"][date][0]["close_approach_data"][0]["miss_distance"]["miles"])
                lunar_dist = lunar_distance(dist_miles)
                print(f"The lunar distance is {round(lunar_dist, 2)} moons\n")
                #print(lunar_dist)
    #print(neojson)

## call main
main()

