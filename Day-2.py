# Day -2
# two_digit_number = input("Type a two digit number: ")
# first_number = two_digit_number[0]
# second_number = two_digit_number[1]
#
# result = int(first_number) + int(second_number)
# print(result)

#
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# bmi = int(weight) / float(height) ** 2
# print(bmi)

# # Age in weeks
# age = input("What is your current age?")
# age_int = int(age)
# years_left = 90 - age_int
# age_in_days = years_left * 365
# age_in_weeks = years_left * 52
# age_in_months = years_left * 12
#
# print(f"You have {age_in_days} days, {age_in_weeks} weeks and {age_in_months} months left")

# Tip calculator
print("Welcome to the tip calculator")
total_bill = input("What was the total bill? ")
total_bill_as_float = float(total_bill)
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
tip_as_float = int(tip) * 0.01
total_amount_payable = total_bill_as_float * (1 + tip_as_float)
total_people = input("How many people to split the bill? $")
total_people_as_int = int(total_people)
split_bill = total_amount_payable / total_people_as_int
rounded_split_bill = round(split_bill, 2)
print(f"Each person should pay: ${rounded_split_bill}")
