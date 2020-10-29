#!/usr/bin/python3
import time

# function building practice
def luis():
    for x in range(1,6):
        print(x*"* ")
    for x in range(4,-1,-1):
        print(x*"* ")
luis()

flags = 0
limit = 9

while  flags < limit:
    print(flags*"* ")
    flags += 1

