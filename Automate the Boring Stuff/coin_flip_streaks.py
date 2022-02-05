"""
Flips a coin x amount of times
Checks to see if a streak  of H was found
"""

import random

results = ""
streak_count = 0

for experimentNumber in range(10000):
    if random.randint(0, 1) == 0:
        results += "H"
    else:
        results += "T"

for char in results:
    if char == "H":
        streak_count += 1
    else:
        streak_count = 0

    if streak_count == 6:
        print("a streak was found")
