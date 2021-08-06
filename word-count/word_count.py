import re
def count_words(sentence):
    words = re.findall("[a-zA-Z0-9]+'*[a-zA-Z0-9]+", sentence)
    words = [i.lower() for i in words]
    result = {}
    for rec in set(words):
        result[rec] = words.count(rec)
    return result


# def count_words(sentence):
#     """Takes a sentence and count the number of unique words."""

#     from collections import Counter

#     words = []
#     place = 0

#     # A word is defined to be a contiguous string of alphanumeric characters,
#     # plus any apostrophes that are enclosed inside it.
#     # Loop through each character to find the starting and ending indexes of
#     # a word, and then use a string slice to append the word to the final list.
#     for index, character in enumerate(sentence):
#         if character.isalnum():
#             continue
#         if character == "'":
#             # Check if the ' character is between two alphanumeric characters.
#             # Using a try/catch to accomodate checking when the ' is the first
#             # or last character in the sentence string.
#             try:
#                 assert sentence[index - 1].isalnum() and sentence[index + 1].isalnum()
#                 # It is, so it's an apostrophe.
#                 continue
#             except (AssertionError, IndexError):
#                 # It is not, so it's a single quote.
#                 pass
#         # Stop looping when we hit a character other than an alphanumeric or
#         # apostophe, and scoop up all of the characters between here and the
#         # previous non-alphanumeric character.
#         words.append(sentence[place:index])
#         place = index + 1
#     words.append(sentence[place:])

#     # Normalize for lowercase and remove blank entries.
#     words = [item.lower() for item in words if item]

#     return Counter(words)