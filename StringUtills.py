import random


def string_to_list(string):
    *list, = string
    return list


def list_to_string(list, separater):
    if separater == True:
        string = " ".join(list)
    elif separater == False:
        string = join(list)

def alternating_case_text(string):
    alternating_text = ""
    for i, char in enumerate(string):
        if i % 2 == 0:
            alternating_text += char.upper()
        else:
            alternating_text += char.lower()
    return alternating_text



def reverse_string(string):
    return string[::-1]


def remove_whitespace(string):
    return ''.join(string.split())



def is_palindrome(string):
    clean_string = remove_whitespace(string).lower()
    return clean_string == clean_string[::-1]

