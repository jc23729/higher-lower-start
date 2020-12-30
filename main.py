from art import logo, vs
from game_data import data
import random


# Display the art
print(logo)

# Generate a random account from game data and split up into two accounts, A and B
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

# How do we format the data account into a printable format//So we know that the data is a dictionary and we accesss with a key value pair


# Ask the user for a guess


# Check if user is correct


# Get the follower count of each account


# Use if statement to check if user is correct

# Give user feedback on their guess

# Score keeping

# Make the game repeatable

# Making account at position B become the next account at position a


# Clear the screen
