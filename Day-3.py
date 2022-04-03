# Conditionals
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# BMI 2.0
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / height ** 2)
#
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are overweight")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese")


# Leap Year Challenge
# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year")

# height = int(input("What is your height in cm "))
# bill = 0
# charge = 0
# extra_charge = 3
#
# if height >= 120:
#     age = int(input("What is your age? "))
#     if age < 12:
#         charge = 5
#         want_photo = input("Do you want a photo? Y or N")
#         if want_photo.lower() == "y" | "yes":
#             bill = charge + extra_charge
#             print(f"Your charge is ${bill}")
#     elif age <= 18:
#         charge = 7
#         want_photo = input("Do you want a photo? ")
#         if want_photo.lower() == "yes":
#             bill = charge + extra_charge
#             print(f"Your charge is ${bill}")
#         else:
#             bill = charge
#             print(f"Your charge is ${bill}")
#     else:
#         charge = 12
#         want_photo = input("Do you want a photo? ")
#         if want_photo.lower() == "yes":
#             bill = charge + extra_charge
#             print(f"Your charge is ${bill}")
#         else:
#             bill = charge
#             print(f"Your charge is ${bill}")
# else:
#     print("You cannot ride the roller coaster!")


# Pizza exercise
print("Welcome to Python Pizza Deliveries")
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_for_small_pizza = 2
pepperoni_for_medium_or_large_pizza = 3
extra_cheese_for_all_sizes = 1
bill = 0
size = input("What size of pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y, N ")
extra_cheese = input("Do you want extra cheese? Y, N ")
#
# if size.lower() != "s" or size.lower() != "m" or size.lower() != "l":
#     print("Please select between letter S, M, L")


if size.lower() == "s":
    if add_pepperoni.lower() == "y":
        if extra_cheese.lower() == "y":
            bill = small_pizza + pepperoni_for_small_pizza + extra_cheese_for_all_sizes
        else:
            bill = small_pizza + pepperoni_for_small_pizza
    else:
        bill = small_pizza
elif size.lower() == "m":
    if add_pepperoni.lower() == "y":
        if extra_cheese.lower() == "y":
            bill = medium_pizza + pepperoni_for_medium_or_large_pizza + extra_cheese_for_all_sizes
        else:
            bill = medium_pizza + pepperoni_for_medium_or_large_pizza
    else:
        bill = medium_pizza
else:
    if add_pepperoni.lower() == "y":
        if extra_cheese.lower() == "y":
            bill = large_pizza + pepperoni_for_medium_or_large_pizza + extra_cheese_for_all_sizes
        else:
            bill = large_pizza + pepperoni_for_medium_or_large_pizza
    else:
        bill = large_pizza

print(f"Your final bill is: ${bill}.")

