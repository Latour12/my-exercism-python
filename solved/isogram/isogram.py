def is_isogram(string):
    new_string = ''.join(i for i in string.lower() if i.isalpha())
    return len(new_string) == len(set(new_string))


# def is_isogram(string):
#     word = ''.join(i for i in string.lower() if i.isalpha())
#     return len(word) == len(set(word))