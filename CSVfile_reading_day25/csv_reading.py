# with open("weather_data.csv") as weather:
#     print(weather.readlines())


import csv
import pandas

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        print(row)
        temperatures.append(row[1])
        print(temperatures)
