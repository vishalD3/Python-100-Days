
#Part 1:
#TODO: 1 : Randomly choose  a word from the word_list and assign it to a variable called chosen_word. then print it
#TODO : 2: Ask user to guess a letter and assign their ans to variable called guess. Make guess lowercase
# TODO: 3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#           print "Right" if it is and "Wrong" if it is not

# Part 2:
# todo: 1: Create empty String called "Placeholder"
# todo: 2 FOr each  letter in the chosen_word, add a _ to a placeholder
# todo: 3 So if the chosen_word is apple placeholder should be _____ with 5 "_" representing each letter to guess


import random
from hangman_word import word_list
from hangman_art import stages,logo
lives = 5


print(logo)
chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder= ""
word_length = len(chosen_word)
for pos in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []
while not game_over:

    print(f"*************************{lives}/5***************************")
    guess = input("Guess a Letter \n").lower()
    if guess in correct_letter:
        print(f"You have already guessed {guess}")
    display= ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

# count live
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(f"**************************** IT WAS {chosen_word} Lose !*****************************")

    if "_" not in display:
        game_over = True
        print("*******************************You Win !*******************************")

    print(stages[lives])


