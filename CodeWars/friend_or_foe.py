"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
"""

# loops through list of persons
# if person is a friend i.e len == 4
# store in list
def friend(x):
    return [person for person in x if len(person) == 4]
