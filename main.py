from art import logo, vs
from game_data import data
import random

# How do we format the data account into a printable format//So we know that the data is a dictionary and we accesss with a key value pair
#this will pull out from the dic
def format_data(account):
  """Format account data into printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return(f"{account_name}, a {account_descr}, from {account_country}")
# Check if user is correct
def check_answer(guess, a_followers, b_followers):
  """use if statement to check if user is correct"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
# Display the art
print(logo)

# Generate a random account from game data and split up into two accounts, A and B
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Compare B: {format_data(account_b)}.")
# Ask the user for a guess
guess = input("Who has more followers? Type 'A' or 'B': ").lower()


# Get the follower count of each account, so we setup a variable a_follower_count and we set it to equal, the account_a pulling from the dict of data
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

# Check if user is correct #######################we're going to move it to TOP and make a reusable function 




# Use if statement to check if user is correct

# Give user feedback on their guess

# Score keeping

# Make the game repeatable

# Making account at position B become the next account at position a


# Clear the screen
