import random


def shuffle_string(input_string):
    char_list = list(input_string)
    random.shuffle(char_list)
    shuffled_string = ''.join(char_list)
    return shuffled_string


print(shuffle_string("Bonjour tout lemonde!"))