print("Welcome...")
answer = input ("Would you like to play? (yes/no) ")

if answer == "yes":

    answer = input("You've found a knife at the end of a trail, do you keep following or head back? (forward/back)")
    
    if answer == "forward":
        answer = input("You have encountered a bear! would you like to run or attack? (run/attack)")

        if answer == "attack":
            print("YOU HAVE DIED!")
            print("Not the smartest choice, the bear has ripped you to pieces!")

        else:
            print("Good choice, you made it away safetly.")

    elif answer == "back":
        print("YOU HAVE DIED!")

    else:
        print("YOU HAVE DIED!")
        print("Invalid Choice, ERROR CODE: 4431")

else:
    print("Shame...")