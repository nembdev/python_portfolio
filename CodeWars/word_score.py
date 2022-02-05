def word_score(string):
    """
    Given a string of words, you need to find the highest scoring word.

    Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
    """
    values = "abcdefghijklmnopqrstuvwxyz"
    scores = []
    words = string.split()
    high_score = 0
    highest_word = ""

    for word in words:
        word_value = 0
        for char in word:
            word_value += values.index(char) + 1

        print(word, word_value)

        if word_value > high_score:
            high_score = word_value
            word_value = 0
            highest_word = word

    return highest_word


word_score("man i need a taxi up to ubud")
