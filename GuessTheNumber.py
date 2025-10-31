import random
import time
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_animation():
    frames = [
        "Congratulations! 🎉",
        "You did it! 🥳",
        "Amazing! 🎉👏",
        "You're a genius! 💡💥"
    ]
    
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.5)

number = random.randint(1, 10)
attempts = 0

print("Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 10.")
print("If you want a hint, type 'hint'.")

while True:
    guess_input = input("Enter your guess: ")

    if guess_input.lower() == "hint":
        if number > 5:
            print("Hint: The number is greater than 5.")
        elif number < 5:
            print("Hint: The number is less than 5.")
        else:
            print("Hint: The number is exactly 5.")
        time.sleep(1)
        continue
    
    try:
        guess = int(guess_input)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print_animation()
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        break
