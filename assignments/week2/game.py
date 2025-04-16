import random
import time

print ("Welcome to the guess the number game!")

name = str(input("What's your name? "))

print("Hi " + name + "!")

age = int(input("How old are you? "))
if age < 6:
    print("You are too young!")
else:
    print("That's nice!")
    print("Generating number")
    time.sleep(1)  # delay 1 second
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")


    max_attempts = int(input("How many attempts do you think you need? "))
    attempts = 0
    number = random.randint(1, 100)

    while attempts < max_attempts:
        guess = int(input(" Guess the number: "))
        if guess < 1 or guess > 100:
            print("Error! Please type a number between 1 and 100.")
        elif guess < number:
            print("go higher")
            attempts += 1
        elif guess > number:
            print("go lower")
            attempts += 1
        else:
            print("Guessed right!")
            attempts += 1
            break
        if attempts >= max_attempts:
            print("You lose...")
