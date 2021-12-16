print("Welcome to TextAdventure v0.0.1")
answer = input ("Would you like to start a new game? (yes/no) ")

if answer == "yes":

    answer = input("You've started walking... a deep dark forrest around you. Here you find a path, hidden behind trees and bush, do you move forward? or head back? (forward/back) ")
    
    if answer == "forward":
        answer = input("You head on into the grassy trail, you hear a branch snap in the distance, a shadow behind the tree ahead, what do you do? (run/attack) ")

        if answer == "attack":
            print("YOU HAVE DIED!")
            print("Not the smartest choice, the killer found you and stabbed you in the heart ")

        else:
            answer = input("Good choice, you hear more noise and run towards the left, you hear more noises behind you as you run faster and faster, the trail comes to a hault, two paths ahead, but which one? (right/left) ")

            if answer == "right":
                print("YOU HAVE DIED!")
                print("The killer found you! he stabbed you in the back of the legs and left you for dead!")

            elif answer == "left":
                answer = input("You made it! After running left for about 3 minutes you hear the crunches and chasing come to a hault, you're not safe yet though, whats next? (run/rest) ")

                if answer == "run":
                    print("")
                
                elif answer == "rest":
                    print("")


    elif answer == "back":
        print("YOU HAVE DIED!")

    else:
        print("YOU HAVE DIED!")
        print("Invalid Choice, ERROR CODE: 4431")

else:
    print("Shame...")