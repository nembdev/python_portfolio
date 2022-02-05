"""
Collatz sequence
a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1
"""
result = 0

# get a number from the user
number = input()

# convert it to an an int
try:
    number = int(number)
except ValueError:
    print("must enter an integer")


def collatz():
    global result
    global number
    result = number // 2 if number % 2 == 0 else 3 * number + 1
    number = result
    print(number)


while result != 1:
    collatz()
