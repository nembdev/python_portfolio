"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
"""


def get_middle(s):
    # your code here
    # even
    if len(s) % 2 == 0:
        middle_two = int(len(s) / 2)
        # print(middle_two)
        return s[middle_two - 1] + s[middle_two]
    else:
        half_index = int((len(s) / 2))
        # print(half_index)
        return s[half_index]


s = "123456"
get_middle(s)

s = "1234567"
get_middle(s)
