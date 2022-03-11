"""
Problem: find out number of occurrences of a number in a sorted array

Algorithm number_occurrence
Input: sorted list l, target t
Output: c count of t

f+l Binary Search
    f = find_first #o(log n)
    l = find_last #o(log n)
    return (last - first + 1)
"""


def fl_binary_search(list, target, search_first):
    l = 0
    h = len(list) - 1
    result = -1

    while l <= h:
        mid = (l + h) // 2
        if list[mid] == target:
            result = mid

            if search_first:
                h = mid - 1
            else:
                l = mid + 1
        elif list[mid] > target:
            h = mid - 1
        else:
            l = mid + 1
    return result


def number_occurrences(list, target):
    # count =
    l = fl_binary_search(list, target, True)
    print(l)
    if l == -1:
        return None
    h = fl_binary_search(list, target, False)
    print(h)
    count = (h - l) + 1

    return print(count)


list = [1, 1, 3, 4, 5, 5, 5, 5, 5, 9, 9, 11]
number_occurrences(list, 9)
