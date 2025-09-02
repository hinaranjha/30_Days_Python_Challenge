# Project: "Unique Word Extractor" from a text

text = input("Enter a word: ")

unique_word = []

for word in text.split():
    if word not in unique_word:
        unique_word.append(word)

print(unique_word)