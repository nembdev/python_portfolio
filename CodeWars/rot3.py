def rot13(message):
    """
    ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
     A function that takes a string and returns the string ciphered with Rot13
    """
    msg_chars = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for char in message:
        for a_char in alpha:
            rot = alpha.index(a_char) + 13
            if char.lower() == a_char || :
                if rot > 25:
                    rot -= 26
                if char.isupper():
                    msg_chars.append(alpha[rot].upper())
                else:
                    msg_chars.append(alpha[rot])
    return "".join(msg_chars)
    print(msg_chars)


rot13("Test")
