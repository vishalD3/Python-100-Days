

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())
phonetic_dic = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dic)

#[key:value for (index,row) in data.iterrow()]:- itrate dataframe row

word= input("Enter a word : ").upper()
output_list = [phonetic_dic[letter] for letter in word]
print(output_list)

#syntax for comprehension [new_item for item in list]