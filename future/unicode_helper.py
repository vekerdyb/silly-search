def remove_non_letters(word):
    return ''.join(letter for letter in word if letter.isalpha())