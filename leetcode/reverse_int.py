'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''


def reverse(num):
    s = str(num)
    split = []
    for char in s:
        split.append(int(char))
    split.reverse()
    print(split)

num = 123
reverse(num)
