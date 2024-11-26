import pandas

data = pandas.read_csv("Squirel_Data.csv")
grey_squirels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirels_count = len(data[data["Primary Fur Color"] == "Black"])
#print(grey_squirels_count)
#print(red_squirels_count)
#print(Black_squirels_count)

data_dict = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirels_count, red_squirels_count, Black_squirels_count]
}

#print(data_dict)

data_Created = pandas.DataFrame(data_dict)
#print(data_Created)
data_Created.to_csv("squirel_count.csv")