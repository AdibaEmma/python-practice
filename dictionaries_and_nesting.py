programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
}

# Retrieving items from a dictionary
print(programming_dictionary["Function"])

# Retrieving items from a dictionary with a fallback value
print(programming_dictionary.get("Bug", "Not Found"))

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"


# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# Loop through a dictionary
# for entry in programming_dictionary:
#     print(f"{entry}: {programming_dictionary[entry]}")


# Grading Program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

for student in student_grades:
    print(f"{student}: {student_grades[student]}")
