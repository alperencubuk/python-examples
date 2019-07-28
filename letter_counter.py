# Letter Counter

def letter_counter(text):
    letters = {}
    for letter in text:
        letters[letter] = letters.get(letter,0) + 1
    return letters


print(letter_counter('AlperenCubuk'))
