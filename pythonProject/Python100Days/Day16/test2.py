from prettytable import PrettyTable

table = PrettyTable()
table.add_column("DOTA Hero", ["Zeus","Axe","Huskar","Mirana"])
table.add_column("Type", ["Mage","Strength","Strength","Agility"])
table.align = "l"
print(table)
