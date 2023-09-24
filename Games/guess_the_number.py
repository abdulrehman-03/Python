logo = """                                                            
 _____                 _____ _       _____           _           
|   __|_ _ ___ ___ ___|_   _| |_ ___|   | |_ _ _____| |_ ___ ___ 
|  |  | | | -_|_ -|_ -| | | |   | -_| | | | | |     | . | -_|  _|
|_____|___|___|___|___| |_| |_|_|___|_|___|___|_|_|_|___|___|_|  
                                                                 
"""

import random

print(logo)

print("Welcome to the Number Guessing Game!")
level = input("Choose a difficulty level. Type 'easy', 'hard' or 'expert': ")

# Default range is 1-100. Will be 1-150 in expert mode
range = 100
# Default attempts are 5. Change in case of easy
attempts = 5

# Changing number of attempts and guessing range based on difficulty level
if level == 'easy':
  attempts = 10
elif level == 'hard':
  attempts = 5
elif level == 'expert':
  range = 150
else:  
  print("You entered wrong level, so giving you the expert one. 😈")
  range = 150

print(f"Guess a number between 1 and {range}.")
number = random.randint(1,range)

# Looping through users guesses
while attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Guess: "))
  # Checking if guess matches the answer
  if guess > number:
    print("Too high.")
  elif guess < number:
    print("Too low.")
  else:
    print(f"You got it! The answer was {number}.")
    break
  attempts -= 1

# Printing you lost message if attempts ends
if attempts == 0:
  print("You've ran out of guesses, you lose.")
