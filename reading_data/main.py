import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# # print(data["temp"])
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
#
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp_F = monday.temp * 9 / 5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# 
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(red_squirrels["Hectare Squirrel Number"])

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(gray_squirrels["Hectare Squirrel Number"])

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels["Hectare Squirrel Number"])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

squirrel_count_data = pandas.DataFrame(data_dict)
squirrel_count_data.to_csv("squirrel_count.csv")
