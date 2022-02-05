#original
def rem_vowels(string_):
    vowels = ["A", "a","E", "e","I", "i","O", "o","U", "u"]
    n_string = ""
    for char in string_:
        if char not in vowels:
            n_string += char

    return n_string #string_

rem_vowels("test")


#best practice 10x faster
#returns a copy of a string
#maps each char to a given iterable object
#None will delete the characters from the string
 str.translate(None, string_)
