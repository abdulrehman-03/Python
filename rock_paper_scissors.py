rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

rnd = random.randint(0,2)

if rnd == 0:
  com_choice = rock
elif rnd == 1:
  com_choice = paper
else:
  com_choice = scissors

user = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user == 0:
  user_choice = rock
elif user == 1:
  user_choice = paper
elif user == 2:
  user_choice = scissors
else:
  print("Please enter a valid number!")
  
if user == rnd:
  result = "Draw!"
elif user == 0 and rnd == 2:
  result = "You won!"
elif rnd > user:
  result = "Computer won!"
elif rnd == 0 and user == 2:
  result = "Computer won!"
else:
  result = "You won!"


print("You chose:")
print(user_choice)

print("Computer chose:")
print(com_choice)

print(result)
