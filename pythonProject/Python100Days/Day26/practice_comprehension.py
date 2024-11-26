

# range_list = [new_item for item in list]
# number_range = [num * 2 for num in range(1,5)]
# print(number_range)


# names = ['Alex', 'Beth', 'Carolina','Dave','Eleanor','Freddie']
#
# captial_name = [name.upper() for name in names if len(name) > 5]
# print(captial_name)

#Square number
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number * number for number in numbers]
# print(squared_numbers)
#
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(i)for i in list_of_strings]
# result = [number for number in numbers if number % 2 ==0]
# print(result)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

#temp to Fer using dict comprehension
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day: temp * 9/5 + 32 for (day,temp) in weather_c.items()}
# print(weather_f)

#Iterate over pandas dataFrame
students_dict = {

    "students" : ["Roy","Tom","Harry","Potter"],
    "score" : [56,78,87,76]
}

# for (key, value) in students_dict.items():
#     print(value)

import pandas
students_dict_frame = pandas.DataFrame(students_dict)
#print(students_dict_frame)

#loop through data frame
# for (key,value) in students_dict_frame.items():
#     print(value)

# loops through rows of dataframe

for(index, row) in students_dict_frame.iterrows():
    if row.students == "Harry":
        print(row.score)