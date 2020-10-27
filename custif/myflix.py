#!/usr/bin/env python3

print(" Who is stronger Goku or Thanos: ")
hero = input().upper()

print(f" You have chosen {hero}, it is time to battle") 

if hero == "GOKU":
    print("Alright Dragon Ball Fun boy")
    print("It's time to Battle")
    print("*******BATTLE***************")
    print("Thanos would beat Goku, Thanos can use the time stone goes to an era where he is weak and kick his butt")
    print("1-How can you even think that Thanos can beat goku, nobody beats goku")
    print("2-Goku would steal the time stone before he uses it")
    answer1g = int(input())
    if answer1g == 1:
        print("Goku was Lit, but you aren't ready for this")
        print("Thanos WON")
        #break
    elif answer1g == 2:
        print("Goku takes the time stone.\nBut ... \nThanos would use the power stone and beat goku")
        print("1-Goku eat a sensu bean and gets 10x stronger")
        print("2-This dude can't do anyhting with out his pebbles")
        answer2g = int(input())
        if answer2g == 1:
            print("Thanos uses the reality stone and creates a world without sensu beans")
            print("1-Goku goes super sayjin 3 and kicks Thanos's butt")
            print("2-Goku goes 'migatte no gokui' and destroys the Gauntlet")
            answer3g = int(input())
            if answer3g == 1:
                print("Super Sayjin 3 was not enought. Thanos WON")
               # break
            elif answer3g == 2:
                print("Goku wins")
               # break
        elif answer2g == 2:
            print("Goku was Lit, but you are not ready for this")
            print("Thanos WON")
           # break
if hero == "THANOS":
    print("Why even bother")
    print("Goku win")


