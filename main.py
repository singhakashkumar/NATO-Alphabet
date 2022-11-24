import pandas

df = pandas.read_csv('./nato_phonetic_alphabet.csv')
nato_dict = {row.letter : row.code for (index, row) in df.iterrows()}

user_input = input("Enter a word: ").upper()
phonetic_list = [nato_dict[character] for character in user_input if character != ' ']
print(phonetic_list)
