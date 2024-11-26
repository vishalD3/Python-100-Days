import random

rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_

'''

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   
'''
scissor ='''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ |
|___/\___|_|___/___/\___/|_|  |___/
'''

game_images = [rock, paper, scissor]

print("Welcome to Rock, Paper and Scissor game !")
user_choice = int(input("what you want choose ? 0 for Rock, 1 for Paper and 2 for Scissor\n"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer Choose: ")
print(game_images[computer_choice])


if user_choice >=3 or user_choice <0:
    print("You have entered invalid number. You Loose!")
elif user_choice == 0 or user_choice ==2:
    print("You Win! ")
elif computer_choice == 0 or computer_choice == 2:
    print("You loose! ")
elif computer_choice > user_choice:
    print("You loose! ")
elif user_choice > computer_choice:
    print("You Win! ")
elif user_choice == computer_choice:
    print("Its A Draw!")



