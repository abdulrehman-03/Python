from replit import clear
from art import logo

print(logo)

# Function to calculate the highest bidder and amount
def highest_bidder(biddings):
  highest_bid = 0
  for bidder in biddings:
    bid_amount = biddings[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"{winner} won with the highest bid of ${highest_bid}")

bids = {}

# Running a loop to input values until user stops
while True:
  name = input("What is your name?: ")
  price = input("Enter your bid: $")
  another = input("Is there anyone else to bid? yes/no:\n").lower()

  # Adding bidder's name and amount to the dictionary
  bids[name] = int(price)
  clear()
  # Breaking the loop and printing results if bidding is done
  if another != "yes":
    highest_bidder(bids)
    break
