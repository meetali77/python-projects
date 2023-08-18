import art
from game_data import data
import random
from replit import clear

def format_data(account):
  """format account data"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_ans(guess, a_followers, b_followers):
  """Takes the user guess and follower counts and returns if they got it right"""
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'
  
# display art
print(art.logo)
score = 0
continue_game = True
account_b = random.choice(data)

# make the game repeatable
while continue_game:
  # random account from data
  # making accounts at position B become position A
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}")
  print(art.vs)
  print(f"Against B: {format_data(account_b)}")
  
  # ask user for guess
  guess = input("Who has more followers? Type 'A' or 'B'': ").lower()
  
  # check if user is correct
  ## compare using if statement
  ## get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_ans(guess, a_follower_count, b_follower_count)

  clear()
  # give user feedback on guess
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    continue_game = False
    print(f"Sorry you're wrong. Final score: {score}")




# clear the screen bet rounds