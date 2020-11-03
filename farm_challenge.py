#!/usr/bin/python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]



for animal in farms[0]["agriculture"]:
    print(animal)

print("Challenge 1 completed")

#Challenge 2 
#Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.


print(" Please choose one the farms (NE Farm/W Farm/SE Farm) to return the plants/animals that are raised on that farm.")
choosen_farm = input().lower()
veggies = ["carrots","celery"]

if choosen_farm == farms[0]["name"].lower():
    for stuff in farms[0]["agriculture"]:
        print(stuff)
elif choosen_farm == farms[1]["name"].lower():
    for stuff in farms[1]["agriculture"]:
        print(stuff)
elif choosen_farm == farms[2]["name"].lower():
    for stuff in farms[2]["agriculture"]:
        if stuff in veggies:
            print(f"No {stuff} in my plate")
        else:
            print(stuff)



print("Challenge 2 completed")



