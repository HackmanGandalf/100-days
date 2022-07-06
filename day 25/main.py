# # with open("100-days-of-code/day 25/weather_data.csv") as weather_data:
# #     data = weather_data.readlines()
# #     print(data)

# # import csv

# # with open("100-days-of-code/day 25/weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperatures = []
# #     for line in data:
# #         if line[1] != "temp":
# #             temperatures.append(int(line[1]))
# #     print(temperatures)
# import pandas

# data = pandas.read_csv("100-days-of-code/day 25/weather_data.csv")
# temp_list = data["temp"].to_list()

# # total_temp = 0
# # for item in temp_list:
# #     total_temp += item
# # print(total_temp / len(temp_list))
# # print(data["temp"].mean)
# # print(data["temp"].max())
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32)

import pandas
data = pandas.read_csv("100-days-of-code/day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("100-days-of-code/day 25/practice.csv")