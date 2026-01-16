# with open("weather_data.csv") as weather:
#     print(weather.readlines())


import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data:
#         print(row)
#         temperatures.append(row[1])
#         print(temperatures)

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(type(data["temp"]) )

# temp = data["temp"].max()
# print(temp)
print(data.condition)

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
print(monday_temp)
monday_temp = monday_temp * 9/5 + 32
print(monday_temp)


