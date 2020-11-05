import json
import time


file= open("mommas.json", "r").read()

mommas= json.loads(file)

#challenge 1
print("First Challenge")

for x in mommas["east_coast_mommas"]:
   # print(x)
    for y in x.keys():
        if y == "name":
            print(x[y])

time.sleep(1)

#challenge 2
print("\nChallenge 2")

for x in mommas.keys():
    #print(x)
    for y in mommas[x]:
        #print(y)
        for z in y.keys():
            #print(z)
            if z == "name":
                print(y[z])

time.sleep(1)

#Challenge 3
print("\nChallenge 3")

for x in mommas.keys():
    #print(x)
    for y in mommas[x]:
        #print(y)
        for z in y.keys():
            #print(z)
            if z == "estimated_diameter":
               # print(y[z]["miles"]["diameter_max"])
                large_momma = y[z]["miles"]["diameter_max"]

                if large_momma == 0.033:
                    print(y["name"])
                    print(f"mommma size is {large_momma}")
                        
#print(mommas)
