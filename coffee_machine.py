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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

"""
Quarters = .25 dollars,
dimes = .10 dollars,
nickles = .05 dollars,
pennies = .01 dollars
"""

should_continue = 1


def recieve():
    quarters = int(input("How many quarters?\n"))
    dimes = int(input("How many dimes\n"))
    nickles = int(input("How many nickles\n"))
    pennies = int(input("How many pennies\n"))

    quarters = quarters * 0.25
    dimes = dimes * 0.10
    nickles = nickles * 0.05
    pennies = pennies * 0.01

    recieved_money = quarters + dimes + nickles + pennies
    return recieved_money


total_money = 0


while should_continue == 1:
    choice = input("What would you like? \n").lower()
    if choice == "report":
        print(f'water: {resources["water"]}\nmilk: {resources["milk"]}\ncoffee: {resources["coffee"]}\n')
    elif choice == "espresso":
        print("Please insert coins.\n")
        money = recieve()
        if money > 1.5:
            bill = money - 1.5
            resources["water"] = resources["water"] - 50
            resources["coffee"] = resources["coffee"] - 18
            print(f"Here is your change ${round(bill, 2)}\n")
            print("Here is your coffee ☕. Enjoy! \n")
            total_money += money
        else:
            print(f"Sorry, Not enough coins inserted, Here is your money back {money}\n")

    elif choice == "latte":
        print("Please insert coins.\n")
        money = recieve()
        if money > 2.5:
            bill = money - 2.5
            resources["water"] = resources["water"] - 200
            resources["coffee"] = resources["coffee"] - 24
            resources["milk"] = resources["milk"] - 150
            print(f"Here is your change ${round(bill, 2)}\n")
            print("Here is your coffee ☕. Enjoy! \n")
            total_money += money
        else:
            print(f"Sorry, Not enough coins inserted, Here is your money back {money}\n")

    elif choice == "cappuccino":
        print("Please insert coins.\n")
        money = recieve()
        if money > 3.0:
            bill = money - 3.0
            resources["water"] = resources["water"] - 250
            resources["coffee"] = resources["coffee"] - 24
            resources["milk"] = resources["milk"] - 100
            print(f"Here is your change ${round(bill, 2)}\n")
            print("Here is your coffee ☕. Enjoy! \n")
            total_money += money
        else:
            print(f"Sorry, Not enough coins inserted, Here is your money back {money}\n")

    elif choice == "off":
        print("Take Care, Have a great day!\n")
        should_continue = 0

    else:
        print("Wrong input.\n")
