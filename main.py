import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row["letter"]: row.code for index, row in data.iterrows()}


def validate_word():
    word = input("Enter a word: ").upper()
    try:
        nato_list = [data_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only english alphabet.")
        return validate_word()
    else:
        return list(dict.fromkeys(nato_list))

nato_alpha = validate_word()
print(nato_alpha)
