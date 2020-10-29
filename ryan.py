print("How am I gonna get out?")
answer = input("a) Break the bed frame b) Check the nightstand for a key--->").strip()
print(answer) 

if answer.lower() != "a" and answer.lower() !="b":
    print("Please answer (a) or (b).")
elif answer.lower() == "a":
    print("The door flies open and a man with an ax comes in, and one slash your head slides off.")
    print("Game over.")
elif answer.lower() == "b":
    print("Finds key on the night stand and unlocks the handcuffs.")
    print("Do I go A) out the window or B) try the door?")


