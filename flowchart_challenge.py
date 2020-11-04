#!/usr/bin/python3
import os

print(""" AM I A HORSE? 
        A HELPFUL FLOWCHART""")

# funtion for handeling question 1
def question1():
    while True:
        print("Are you a horse?")
        response = input("(no/yes/maybe)\n").lower()
        if response == "no":
            print("You're not a horse.")
            exit()
        elif response == "yes":
            question2()
        elif response == "maybe":
            question2()
        elif response == "q":
            exit()
        else:
            print("Please try again.")

# function for handeling question 2

def question2():
    while True:
        print("How many legs do you walk on?")
        response = input("(2 or 4)\n").lower()
        if response == "2":
            print("You're not a horse.")
            exit()
        elif response == "4":
            question3()
        elif response =="q":
            exit()
        else:
            print("Please try again")

# function for handeling question 3

def question3():
    while True:
        print("Really?")
        response = input("(yes/no)\n").lower()
        if response == "yes" or response == "no":
            question4()
        elif response == "q":
            exit()
        else:
            print("Please try again.")
# function for handeling question 4

def question4():
    while True:    
        print("Can you read and write?")
        response = input("(yes/no)\n").lower()
        if response == "yes":
            print("You're not a horse.")
            exit()
        elif response == "no":
            question5()
        elif response == "q":
            exit()
        else:
            print("Please try again.")

# function for handeling question 5

def question5():
    while True:
        print("Liar, You're reading this.\n")
        response = input("yes or yes\n").lower()
        if response == "yes":
            print("You're not a horse.")
            exit()
        elif response == "q":
            exit()
        else:
            print("Please try again")


question1()




