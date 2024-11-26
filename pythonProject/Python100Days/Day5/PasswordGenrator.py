import random

letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
          "U","V","W","X","Y","Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
          "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

number = ["0","1","2","3","4","5","6","7","8","9"]

symbol = ["@", "#", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", "~", "`"]

#easyWay:


charLetter = int(input("How many letters you want: \n"))
num = int(input("How many numbers you want: \n"))
num_symbol = int(input("How many symbol you want: \n"))

password = ""
#for char in range(0,charLetter):
#    password +=random.choice(letter)

#for char in range(0, num):
#    password += random.choice(number)

#for char in range(0, num_symbol):
#    password += random.choice(symbol)

#print(password)

#Hard way:
password_list = []
for char in range(0,charLetter):
    password_list.append(random.choice(letter))

for char in range(0, num):
    password_list.append(random.choice(number))

for char in range(0, num_symbol):
    password_list.append(random.choice(symbol))

random.shuffle(password_list)

for char in password_list:
    password += char
print(password)