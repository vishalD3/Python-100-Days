import random
from art import logo
easy_attempt_turns = 10
hard_attempt_turns = 5


#function to check users guess against actual answer

def check_answer(user_guess, actual_answer, turns):
    """Check answer against guess, return actual number of turns remaining"""
    if user_guess > actual_answer:
        print("Too High")
        return turns -1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"you got it correct! The correct answer is {actual_answer}")

#function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'hard' or 'easy': ").lower()
    if level == 'easy':
        return easy_attempt_turns
    else:
        return  hard_attempt_turns


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between  1 and 100 ")
    #choose random number between 1 to 100
    answer = random.randint(1,100)
    #print(f"Answer is as hint is: {answer}")


    turns = set_difficulty()


    guess =0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #let user guess the number:
        guess = int(input("Guess the number "))
        turns = check_answer(guess, answer,turns)
        if turns ==0:
            print("You loose, Out of turns")
            return
        if guess != answer:
            print("Guess Again")

game()