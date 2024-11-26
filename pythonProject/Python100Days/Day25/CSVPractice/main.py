# with open("weather_data.csv") as weather_file:
#     new_weather_data = weather_file.readlines()
#     print(new_weather_data)

import csv
from sndhdr import test_aifc

# with open("weather_data.csv") as datafile:
#         data = csv.reader(datafile)
#         temperatures = []
#         print(data)
#         for row in data:
#             #print(row)
#             if row[1] != "temp":
#                 temperatures.append(int(row[1]))
#         print(temperatures)


import pandas


data = pandas.read_csv("weather_data.csv")
#print("data")
#print(data["temp"])

#to dict
# dict_data = data.to_dict()
#print(dict_data)

#to list

# temp_list = data["temp"].tolist()
# print(temp_list)
#print(temp_list[2])
# avg = sum(temp_list)/len(temp_list)
#print(avg)

# max_temp = data["temp"].max()
# print(max_temp)

# print(data[data.day =="Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(f"Tempeature to be converted to Fahrenheit: {monday_temp_f}")


#create data frame from scratch

dat_dict = {
    "students": ["Vishal", "Rajan", "Harshad"],
    "score" : [76,87,90]
}

data_created = pandas.DataFrame(dat_dict)
data_created.to_csv("new_dataCreated.csv")
#print(data_created)