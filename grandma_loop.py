#!/usr/bin/env python3

# Procedure 1 - Counter
# For every [broccoli] I find on your [plate] I'm going to [slap you].
import time


leftover_plate = [ "broccoli","broccoli","broccoli","broccoli","broccoli","broccoli","broccoli",]
count = 0
slaps = [" ZAP!!", "CLANK!!", "POW!!", "BAM!!", "KAPOW!!!"]

for broccoli in leftover_plate:
    count += 1
    print(f"There is a broccoli")
    time.sleep(1.5)
    print(f"{slaps[(count-5)]}")
    time.sleep(0.5)
print(f" Grandma slap you {count} times!")

print("\n############################################")


# Procedure 2 Delete
#For every[bad word] that [you say] I'm going to [slap a tooth out] of your [mouth].


bad_words = ["$%#%&","$%#%&","$%#%&","$%#%&","$%#%&","$%#%&","$%#%&","$%#%&" ]

mouth = 32
count_t = 0
teeth= 1
for curse in bad_words:
    mouth = mouth - teeth
    count_t += 1
    print(f" I heard you said {curse},SLAP!! you have {mouth} tooth left")
    time.sleep(1)
    #mouth = mouth - teeth
print(f"Grandma knock out {count_t} tooth out of your mouth")

print("\n############################################")

# Procedure 3 Add
# For every [lego] I find on the [floor], your dad will put another [dollar] in my [money jar].

legos_floor = ["lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego" ,"lego"]
money_jar = []

increments = 1

for lego in legos_floor:
    money_jar.append("dollar")
    print(f"{len(money_jar)} lego on the floor, so dad adds {increments} dollar to my money jar")
    time.sleep(0.5)
print(f"Easy money, grandma's money jar has extra {len(money_jar)} dollars")




