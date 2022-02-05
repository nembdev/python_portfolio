#original
def is_isogram(string):
    freq = {}
    #makes a frequency table
    for char in string.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    for row in freq:
        if freq[row] >= 2:
            return False
    return True

is_isogram("ab")

#shorter/faster
#set turns the string into a set of unique values
#compares the length of the two strings
#if not equal it is not a isogram
def is_isogram(string):
    return len(string) == len(set(string.lower()))
