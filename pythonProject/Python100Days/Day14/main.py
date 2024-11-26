# Display art
from art import logo , vs
from game_data import data
import random

def format_data(account):
    """ Takes the account data and return printable format"""
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return f"{account_name}, a{account_des}, from{account_country}"

def check_answer(user_guess, a_follower, b_follower):

    """ Takes the user guess and followers counts and return if they got it right """
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Generate a random account  from the dame data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers ? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)

    # check if user is correct
    ## get follower count for each account

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ## Use if statement to check if user is correct.
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    # Give user feedback  on their  guess
    # Score keeping

    if is_correct:
        score += 1
        print(f"You are correct. Current score: {score}")
    else:
        print(f"You are wrong. Final score: {score}")
        game_should_continue = False
# Make game repeatable



# making account at position B  become the next account at position A