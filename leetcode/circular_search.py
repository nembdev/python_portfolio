"""
Given a circularly sorted integer array, find the total number of times the array is rotated. Assume there are no duplicates in the array, and the rotation is in the anti-clockwise direction.

Input:  nums = [8, 9, 10, 2, 5, 6]
Output: The array is rotated 3 times


Input:  nums = [2, 5, 6, 8, 9, 10]
Output: The array is rotated 0 times
"""

"""
Algorithm: binary search ciruclar
    find the pivot point
    check prev and next values
        if <= prev and  <= next
            pivot point
            return index

"""


def circular_search(c2):
    l = 0
    h = len(list) - 1

    while low <= high:
        # not rotated
        if c2[l] <= c2[h]:
            return low

        # mid is pivot point
        midpoint = l + h // 2
        next = (midpoint) + 1 % len(c2)
        prev = (midpoint - 1) + len(c2) % len(c2)

        if c2[midpoint] <= c2[next] and c2[midpoint] <= c2[prev]:
            return midpoint
        elif c2[midpoint] >= c2[l]:
            l = midpoint + 1
        else:
            h = midpoint - 1
    return None


# how many rotations
c2 = [12, 13, 1, 4, 7, 8, 9]
print(circular_search(c2))
