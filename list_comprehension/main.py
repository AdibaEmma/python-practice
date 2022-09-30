# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # squared_numbers = [number ** 2 for number in numbers]
#
# result = [number for number in numbers if number % 2 == 0]
# print(result)

with open("file1.txt") as file1:
    data1 = file1.readlines()
with open("file2.txt") as file2:
    data2 = file2.readlines()
result = [int(num) for num in data1 if num in data2]

print(result)
