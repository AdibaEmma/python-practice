# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # squared_numbers = [number ** 2 for number in numbers]
#
# result = [number for number in numbers if number % 2 == 0]
# print(result)

# with open("file1.txt") as file1:
#     data1 = file1.readlines()
# with open("file2.txt") as file2:
#     data2 = file2.readlines()
# result = [int(num) for num in data1 if num in data2]
#
# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence_list = sentence.split()
#
# result = {word: len(word) for word in sentence_list}
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {key: (value * 9/5) + 32 for (key, value) in weather_c.items()}

print(weather_f)