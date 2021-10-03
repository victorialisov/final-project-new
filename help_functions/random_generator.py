import string
import random


def random_word_generator(letters_number: int = 8):
    letters = string.ascii_lowercase
    word = ''.join(random.choice(letters) for i in range(letters_number))
    return word
