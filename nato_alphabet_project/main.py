import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_coding = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ")
phonetic_code_words = [nato_alphabet_coding[letter.upper()] for letter in word]
print(phonetic_code_words)
