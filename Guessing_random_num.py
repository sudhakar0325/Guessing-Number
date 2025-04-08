import random

print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))
print(f"Hello {name.upper()}, you are {age} years old")

if age >= 8:
    print("You are old enough to play")
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
        gameinp = input("Guess a number between 1-10: ")
        ran = random.randint(1, 10)
        if gameinp.isdigit():
            if int(gameinp) == ran:
                print("You Won Congrats!")
            else:
                print(f"Try Again... The number was {ran}")
        else:
            print("You are so smart... Please enter a number")
    else:
        print("See you later..")
else:
    print("You are not eligible to play this game...")