"""
Algorithm binary_search - findFirstOccurrence
finding first or last occurrence of a number
input: sorted list with duplicates l, target t
output 1: Index of first occurrence of x or None
output 2: Index of last occurrence of x or None
"""
list = [2, 4, 10, 10, 10, 18, 20]
target = 10

# modify the binary search to continue searching even on finding the target element
# update the result to mid and search towards the left
def findFirstOccurrence(list, target):
    l = 0
    h = len(list) - 1

    result = -1

    while l < h:
        mid = (l + h) // 2
        if list[mid] == target:
            # store mid
            result = mid
            # move left to check for an earlier mid
            h = mid - 1
        elif list[mid] < list[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return result


# modify the binary search to continue searching even on finding the target element
# update the result to mid and search towards the left
def findLastOccurrence(list, target):
    l = 0
    h = len(list) - 1

    while l <= h:
        mid = (l + h) // 2
        if list[mid] == target:
            result = mid
            l = mid + 1
        elif list[mid] < h:
            h = mid - 1
        else:
            l = mid + 1
    result


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
