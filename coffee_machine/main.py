from typing import Dict

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

# TODO: 1. Print report
# TODO: 2. Check resources sufficient to make drink order

machine_on = True


def print_report():
    """Prints resources available"""
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]

    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")


def check_resources(required_water, required_coffee, required_milk=0):
    """Checks that resources are sufficient to make coffee"""
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]

    if required_water > water:
        print("Sorry there is not enough water.")
    elif required_coffee > coffee:
        print("Sorry there is not enough coffee.")
    elif required_milk > milk:
        print("Sorry there is not enough milk.")
    else:
        return "sufficient"


coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01
}


def process_coins(inserted_coins):
    """Takes inserted coins and returns total monetary value of the coins"""
    total_monetary_value = 0

    coins_list = inserted_coins.split(', ')

    for coin in coins_list:
        quantity = int(coin.split()[0])
        value = coin.split()[1]
        monetary_value = coins[value]
        total_monetary_value += quantity * monetary_value

    return total_monetary_value


def check_transaction_successful(total_coins_value, coffee_cost):
    """Checks that user inserted right amount of coins and offers change if more"""
    transaction_successful = True

    if total_coins_value > coffee_cost:
        resources["money"] = coffee_cost
        change = total_coins_value - coffee_cost
        print(f"Here is ${round(change, 2)} dollars in change")

    elif total_coins_value == coffee_cost:
        resources["money"] = coffee_cost

    else:
        transaction_successful = False
        print("Sorry that's not enough money. Money refunded.")

    return transaction_successful


def make_coffee(coffee_type: str):
    """Checks if transaction successful and there is enough resources then makes the drink"""
    if coffee_type == "cappuccino" or coffee_type == "latte":
        drink = MENU[coffee_type]
        print(drink)

        water_used = drink['ingredients']['water']
        coffee_used = drink['ingredients']['coffee']
        milk_used = drink['ingredients']['milk']

        resources_status = check_resources(water_used, coffee_used, milk_used)

        if resources_status == "sufficient":
            inserted_coins = input("Insert coins (E.g. 1 quarter, 2 dimes): ")
            print(process_coins(inserted_coins))
            total_coins_value = process_coins(inserted_coins)
            drink_cost = drink["cost"]
            transaction_successful = check_transaction_successful(total_coins_value, drink_cost)

            if transaction_successful:
                resources["water"] -= water_used
                resources["coffee"] -= coffee_used
                resources["milk"] -= milk_used
    else:
        drink = MENU[coffee_type]
        water_used = drink['ingredients']['water']
        coffee_used = drink['ingredients']['coffee']
        print(drink)

        resources_status = check_resources(water_used, coffee_used)

        if resources_status == "sufficient":
            inserted_coins = input("Insert coins (E.g. 1 quarter, 2 dimes): ")
            print(process_coins(inserted_coins))
            total_coins_value = process_coins(inserted_coins)
            drink_cost = drink["cost"]
            transaction_successful = check_transaction_successful(total_coins_value, drink_cost)

            if transaction_successful:
                resources["water"] -= water_used
                resources["coffee"] -= coffee_used


while machine_on:
    option = input("What would you like? (espresso/latte/cappuccino): ")

    if option == "report":
        print_report()
    elif option == "off":
        machine_on = False
    else:
        make_coffee(option)
