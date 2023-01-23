import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row["letter"]: row.code for index, row in data.iterrows()}
name = input("Enter name: ").upper()
nato_alpha = [data_dict[letter] for letter in name if letter in data_dict.keys()]
print(nato_alpha)