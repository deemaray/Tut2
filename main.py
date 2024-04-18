# Tutorial 2
import random
Game =  []

while True:
    name = input("Enter a name: ")
    if name == "" :
        Game.append(name)
    else :
        print(" i should pick a name at random from the list provided .")
        break

randomchoice = random.choice(Game)

while True:
    Usersguess = input("What is the name I am thinking of? ")
    if Usersguess == randomchoice:
        print("Congratulations! You guessed it right!")
        break
    elif Usersguess > randomchoice:
        print("No, it's after that.")
    else:
        print("No, it's before that.")

        
