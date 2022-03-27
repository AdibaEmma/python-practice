# print("Welcome to the Band Name Generator")
#
# city = input("which city did you grow up in?\n")
# pet = input("What's the name of your pet?\n")
#
#
# print("Your band name could be " + city + " " + pet)

# Day -2
# two_digit_number = input("Type a two digit number: ")
# first_number = two_digit_number[0]
# second_number = two_digit_number[1]
#
# result = int(first_number) + int(second_number)
# print(result)


# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# bmi = int(weight) / float(height) ** 2
# print(bmi)

# Age in weeks
age = input("What is your current age?")
age_int = int(age)
expected_age = 90 - age_int
age_in_days = expected_age * 365
age_in_weeks = expected_age * 52
age_in_months = expected_age * 12

print(f"You have {age_in_days} days, {age_in_weeks} weeks and {age_in_months} months left")

