import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row["letter"]: row.code for index, row in data.iterrows()}
while True:
    name = input("Enter name: ")
    name = name.upper().strip()
    for letter in name:
        if letter in data_dict.keys() or letter == " ":
            pass
        else:
            name = input("Please enter letters in alphabet only.\nEnter name: ")
            continue
    break

nato_alpha = []
for letter in name:
    if letter in data_dict.keys() and data_dict[letter] not in nato_alpha:
        nato_alpha.append(data_dict[letter])
print(nato_alpha)