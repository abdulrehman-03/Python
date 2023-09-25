import art
from replit import clear
import random
from data import data

# Storing data in a list in organized way
def useful_data(list):  
  sorted_list = [list['name']]
  sorted_list.append(list['description'])
  sorted_list.append(list['country'])
  sorted_list.append(list['follower_count'])
  return sorted_list

sec_acc = random.choice(data)
game_should_continue = True
score = 0

while game_should_continue:
  first_acc = sec_acc
  sec_acc = random.choice(data)
  
  if first_acc == sec_acc:
    sec_acc = random.choice(data)
  
  data1 = useful_data(first_acc)
  data2 = useful_data(sec_acc)
  
  print(art.logo)
  print(f"Compare A: {data1[0]}, a {data1[1]}, from {data1[2]}.")
  print(art.vs)
  print(f"Against B: {data2[0]}, a {data2[1]}, from {data2[2]}.")
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  followers_1 = data1[3]
  followers_2 = data2[3]
  
  if followers_1 > followers_2:
    answer = 'a'
  else:
    answer = 'b'
  
  if guess == answer:
    clear()
    score +=1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}.")
    
