import random
from replit import clear
from art import logo

# Deck of cards for blackjack
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to print current score
def current_score(comp, user_data, user_total):
    print(f"\n   Your cards: {user_data}, current score: {user_total}")
    print(f"   Computer's first card: {comp}\n")

# If ace is present in deck and score went over 21, then ace value will become 1
def ace_rule(cards, score):
  if 11 in cards and score > 21:
    cards.remove(11)
    cards.append(1)
  return cards
  
# Function to calculate computers hands and score
def comp_dealings(comp_total, comp_cards):
  # Deal a new card to computer until total score is less than 17
  while comp_total < 17:
    comp_new_card = random.choice(cards)
    comp_cards.append(comp_new_card)
    comp_total = sum(comp_cards)
    # In case of a blackjack
    if comp_total == 21 and len(comp_cards) == 2:
      comp_cards = [11, 10]
    # Ace rule
    comp_cards = ace_rule(comp_cards, comp_total)
  # Returning computers final hand
  return comp_cards

# Function to calculate users hands and score
def user_dealings(user_cards):
  # Calculate and update users score and hand each time function is called
  user_new_card = random.choice(cards)
  user_cards.append(user_new_card)
  user_total = sum(user_cards)
  # Ace rule
  user_cards = ace_rule(user_cards, user_total)
  return user_cards

# Function to print final results at the end of a game
def final_result(user_final_hand, user_final_score, comp_final_hand, comp_final_score):
  print(f"\n   Your final hand: {user_final_hand}, final score: {user_final_score}")
  print(f"   Computer's final hand: {comp_final_hand}, final score: {comp_final_score}\n")



play = 'y'
# Looping through the game

while play == 'y':
  play = input("\nDo you want to play a game of blackjack? Type 'y' or 'n': ")
  # Break if user don't want to play
  if play != 'y':
    print("Good bye!")
    break

  clear()
  print(logo)
  
  # Dealing random cards
  user_card1 = random.choice(cards)
  user_card2 = random.choice(cards)
  comp_card1 = random.choice(cards)
  comp_card2 = random.choice(cards)

  # Users hand and total score
  user = [user_card1, user_card2]
  user_data = user
  user_score = sum(user)
  user_data = ace_rule(user_data, user_score)

  # Computers hand and total score
  comp_list = [comp_card1, comp_card2]
  comp_score = comp_card1 + comp_card2
  comp_list = ace_rule(comp_list, comp_score)

  # Printing current score after first dealing
  current_score(comp_card1, user, user_score)

  # In blackjack's case
  if comp_score == 21:
    print(f"\n   Computer's final hand: {comp_list}, final score: {comp_score}")
    print("Lose, opponent has blackjack 😱")
    continue
  elif user_score == 21 and len(user_data) == 2:
    print(f"\n   Your final hand: {user_data}, final score: {user_score}")
    print("Win with a Blackjack 😎")
    continue
    
  # Calculating final hand and score of computer
  comp_data = comp_dealings(comp_score, comp_list)
  comp_score = sum(comp_data)
  
  # Whether user wants a new card
  round = input("\nType 'y' to get another card, type 'n' to pass: ")

  # Dealing a new card and calculating latest hand and score of user
  while round == 'y':
    user_data = user_dealings(user)
    user_score = sum(user_data)
    # Stop asking for new card if user score exceeds 21
    if user_score > 21:
      break
    current_score(comp_card1, user, user_score)
    round = input("\nType 'y' to get another card, type 'n' to pass: ")

  # Printing final hand and score of both players
  final_result(user_data, user_score, comp_data, comp_score)

  # Printing results
  if comp_score > 21 and user_score > 21:
    print("You both went over. Draw 😒")
  elif user_score > 21:
    print("You went over. You lose 😭")
    continue
  elif comp_score > 21 and user_score < 22:
    print("You win 😃")
  elif user_score == comp_score:
    print("Draw 🙃")
  elif user_score < comp_score:
    print("You lose 😤")
  elif user_score > comp_score:
    print("You win 😃")
