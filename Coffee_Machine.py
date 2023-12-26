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
    "coffee": 100, }

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g") 
    print(f"Money: ${profit}")

def report():
    print(resources,"ml")

def check_ingredients(ingredient_input):
    for item in ingredient_input:
        if ingredient_input[item] >= resources[item]:
            print("Sorry we do not have enough resources to make you drink")
            return False
    return True


def coin_processor():
    print("Please insert your coins:")
    quarters = int(input("How many quarters will you enter: ")) * 0.25
    dimes = int(input("How many dimes will you enter: ")) * 0.10
    nickles = int(input("How many nickles will you enter: ")) * 0.05
    pennies = int(input("How many quarters will you enter: ")) * 0.01
    total = quarters + dimes + pennies + nickles
    return total


def transaction_checking(money_inserted,drink_cost):
    if money_inserted < drink_cost:
        print("You do not have enough money to purchase this drink")
        return False
    elif money_inserted >= drink_cost:
        global profit
        profit += drink_cost
        change = money_inserted - drink_cost
        print(f"Your change is ${round(change,2)}, have a good day")
        return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}, Enjoy!")

is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]
        if check_ingredients(drink["ingredients"]):
            money = coin_processor()
            if transaction_checking(money, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



        