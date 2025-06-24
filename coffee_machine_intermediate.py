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
    "cost" : 0,
}

money = 0
coffe_machine = True #its ON

def is_resources_checker(order_ingredients):
    """Returns true is there is enough resources to make the drink, else it returns false"""
    for item in order_ingredients:
         if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def total_coins():
    """Returns the total of the coins inserted by the user"""
    print("Please insert coins")
    quarters = int(input("Enter the no.of quarters you put in: \t")) * 0.25
    dimes = int(input("Enter the no.of dimes you put in: \t")) * 0.1
    nickles = int(input("Enter the no.of nickles you put in: \t")) * 0.05
    pennies = int(input("Enter the no.of pennies you put in: \t")) * 0.01

    total = quarters + dimes + nickles + pennies
    return total

def is_transaction_successful(money_recived, drink_cost,):
    """Return true is the transaction is successful, else return false"""
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        global money
        money += drink_cost
        print(f"Here is ${change} change.")
        return True
    else:
        print("Sorry that isn't enough money, your money is refunded")
        return False


def make_coffe(drink_name, order_ingredients):
    """Deduct the required ingredients form the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")
    # global coffe_machine
    # coffe_machine = False #turns off the coffe machine



while coffe_machine:
    user_choice_drink = input("What would you like (espresso/latte/cappuccino):\t").lower()
    if user_choice_drink == "off":
        coffe_machine = False
    elif user_choice_drink == "report":
        print(f"Water : {resources["water"]}ml")
        print(f"Milk : {resources["milk"]}ml")
        print(f"Coffee : {resources["coffee"]}g")
        print(f"Money : ${money}")
    else:
        drink = MENU[user_choice_drink]
        if is_resources_checker(drink["ingredients"]):
            payment = total_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(user_choice_drink,drink["ingredients"])
