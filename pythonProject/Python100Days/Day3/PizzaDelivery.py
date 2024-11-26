print("Welcome to Pizza Deliveries ")
size = input("What size of pizza do you want ? S, M , L: ")
paneerPizza = input("Do want Paneer Pizza ? Y or N: ")
extra_Cheese = input("Do want extra Cheese ? Yes or NO ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill +=20
elif size == "L":
    bill +=25
else:
    print("You entered wrong choice, Please check!")

if paneerPizza == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3

# Add extra Cheese
if extra_Cheese == "Yes":
    bill += 2

print(f"Your final bill is ${bill}.")

