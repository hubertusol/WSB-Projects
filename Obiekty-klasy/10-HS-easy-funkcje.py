
def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return all(letter in string.lower() for letter in alphabet)
    