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
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]

    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")


def check_resources(required_water, required_coffee, required_milk = 0):
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]

    if required_water > water:
        print("Sorry there is not enough water.")
    elif required_coffee > coffee:
        print("Sorry there is not enough coffee.")
    elif required_milk > milk:
        print("Sorry there is not enough milk.")


def make_coffee(coffee_type: str):
    if coffee_type == "cappuccino" or coffee_type == "latte":
        drink = MENU[coffee_type]
        print(drink)

        water_used = drink['ingredients']['water']
        coffee_used = drink['ingredients']['coffee']
        milk_used = drink['ingredients']['milk']

        check_resources(water_used, coffee_used, milk_used)
        resources["water"] -= water_used
        resources["coffee"] -= coffee_used
        resources["milk"] -= milk_used
    else:
        drink = MENU[coffee_type]
        water_used = drink['ingredients']['water']
        coffee_used = drink['ingredients']['coffee']
        print(drink)

        check_resources(water_used, coffee_used)
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
