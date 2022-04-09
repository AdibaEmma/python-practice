import random

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# total_height = 0
# total_students = 0
# for height in student_heights:
#     total_height += height
#     total_students += 1
# average_height = round(total_height / total_students)
# print(f"Average student height = {average_height}")

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# max_score = 0
# number_of_students = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
#
#
# print(f"The highest score in the class is: {max_score}")

# total = 0
# for n in range(1, 101):
#     total += n
# print(total)
#
# even_total = 0
# for n in range(1, 101):
#     if n % 2 == 0:
#         even_total += n
# print(even_total)
#
# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

print("Welcome to PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_length = nr_letters + nr_symbols + nr_numbers
password = ""

for a in range(1, nr_letters + 1):
    password += random.choice(letters)

for s in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for n in range(1, nr_numbers + 1):
    password += random.choice(numbers)

p = list(password)
random.shuffle(p)
shuffled_password = ''.join(p)

print(shuffled_password)
