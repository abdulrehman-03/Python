# A fun little game build using conditional statements. Do you have what it takes to get to the treasure? Show us!
# Keeping the code messy so you do it the right way by running the code

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
turn = input("Do you wanna go left or right? ").lower()
if turn == "left":
  cave = input("There is a cave ahead, explore or stay? ").lower()
  if cave == "stay":
    beast = input("Beasts are following you. run or fight? ").lower()
    if beast == "run":
      print("You fell into a well. Game Over!")
    elif beast == "fight":
      rest = input("You scared the beasts. It's getting late. rest or eat? ").lower()
      if rest == "rest":
        print("Monster killed you in your sleep. Game Over!")
      else:
        print("Food was poisonous. Game Over!")
    else:
      print("run, fight or Die! You choose to Die. Game Over!")
  elif cave == "explore":
    door = input("3 doors ahead! Which one you wanna go into? red, blue or green? ").lower()
    if door == "red":
      print("Red is always danger! There was fire inside. Game Over!")
    elif door == "blue":
      print("Gorrilas inside. They ate you. Game Over!")
    elif door == "green":
      garden = input("You are inside a garden. dig, rest or leave? ").lower()
      if garden == "dig":
        print("Yayyy! You found the treasure! Well done!")
      elif garden == "rest":
        print("Someone took the treasure while you were sleeping. Game Over!")
      elif garden == "leave":
        print("You were very close to the treasure but you turned away. Game Over!")
      else:
        print("Wrong choice. Garden swallowed you! Game Over!")
    else:
      print("You entered the wrong door. Game Over!")
  else:
    print("You tried to be sneaky so the wolfs ate you. Game Over!")
elif turn == "right":
  print("Pirates found you. Game Over!")
else:
  print("You went against the rules and died. Game Over!")
