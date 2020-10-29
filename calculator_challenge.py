#!/usr/bin/python3
### Defining the arihmetic operation functions
# add function
def add(num1, num2):
    result = num1 + num2
    print(result)
# substract function

def substract(num1, num2):
    result = num1 - num2
    print(result)
# multiply function

def multiply(num1, num2):
    result = num1 * num2
    print(result)
# divide function

def divide(num1, num2):
    result = num1 / num2
    print(result)
# function to get inputs 
def number1():
    num1 = float(input("\n Plese enter a number: "))
    return num1
def number2():
    num2 = float(input("\n Plese enter a second number: "))
    return num2

#ensure second input is greater than zero when calling divide function
def number2_div():
    num2 = float(input(" Please enter a second number: "))
    if num2 < 1:
        while num2 < 1:
            print("This is a division")
            print("Type a number greater than zero")
            num2 = float(input(" Please enter a second number: ")) 
    return num2
#variables
num1 = 0 
num2 = 0

print(" Alta3 Calculator ")

while True:

    print("Please select the arithmetic operation by typing '+', '-', '/', '*'. Or type 'q' to exit.")
    arithmetic_operation = input()
    
    if arithmetic_operation =="q" or arithmetic_operation == "Q":
        break

    elif arithmetic_operation == "+":
       num1 = number1()
       num2 = number2()
       add(num1,num2)

    elif arithmetic_operation == "-":
       num1 = number1()
       num2 = number2()
       substract(num1,num2)

    elif arithmetic_operation == "*":
       num1 = number1()
       num2 = number2()
       multiply(num1,num2)

    elif arithmetic_operation == "/":
       num1 = number1()
       num2 = number2_div()
       divide(num1,num2)
    else:
       print(" Please follow the instruction. Try again")

    

