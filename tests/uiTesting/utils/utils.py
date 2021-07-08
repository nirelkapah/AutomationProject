import random
import string
import re


def generate_random_name():
    letters = string.ascii_letters
    letters_random = ''.join(random.choice(letters) for i in range(3))
    numbers = string.digits
    numbers_random = ''.join(random.choice(numbers) for i in range(3))
    punctuation = string.punctuation
    punctuation_random = ''.join(random.choice(punctuation) for i in range(3))
    return " ".join([letters_random, numbers_random, punctuation_random])


def generate_random_text():
    letters = string.ascii_letters
    letters_random = ''.join(random.choice(letters) for i in range(10))
    numbers = string.digits
    numbers_random = ''.join(random.choice(numbers) for i in range(10))

    return " ".join([letters_random, numbers_random])


def generate_string_to_url(original_string: str):
    output_str = re.sub('[^A-Za-z0-9]+', ' ', original_string).lower().rstrip().lstrip().replace(" ", "-")
    return output_str





