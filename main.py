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
input("Who has more followers? Type 'A' or 'B': ").lower

# Check if user is correct


# Get the follower count of each account


# Use if statement to check if user is correct

# Give user feedback on their guess

# Score keeping

# Make the game repeatable

# Making account at position B become the next account at position a


# Clear the screen
