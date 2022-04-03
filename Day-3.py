# Conditionals
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# height = int(input("What is your height in cm "))
#
# if height >= 120:
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Your charge is $5")
#     elif age <= 18:
#         print("Your charge is $7")
#     else:
#         print("Your charge id $12")
# else:
#     print("You cannot ride the roller coaster!")


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
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a leap year.")
    else:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")
