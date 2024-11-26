MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Todo 1: Print Report
#Todo 2: Prompt User by taking choice (espresso/latte/cappuccino)
#Todo 3: Turn off coffee button: If off word is used it turn off. Code should stop
#Todo 4: Check resources is sufficient
#Todo 5: Process coins
#Todo 6: Check transaction is successful
#Todo 7.1: Make Coffee
#Todo 7.2: All is deducted. Tell user here is your latte. Enjoy!




#Check resources is sufficient
def is_resources_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"Sorry there is not enough {item}")
           is_enough = False
    return is_enough

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.25
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that nor enough money, Please return")
        return False

def make_coffee(drink_name, order_ingredient):
    """Deduct the required  ingredient from the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name} ☕")

# Print Report
# Prompt User by taking choice (espresso/latte/cappuccino)

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        print("Coffee Machine has been Turn off")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])
