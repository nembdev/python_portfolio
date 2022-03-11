"""
Given a sorted array of n integers and a target value, determine if the target exists in the array or not in logarithmic time. If the target exists in the array, return the index of it.

Algorithm Exponential Search(lin+bin) - O(log n)
input: sorted infinite array a, target t
output: index of t or -1

Given a monotonically increasing function f(x) on positive numbers, find the value of x when f(x) becomes positive for the first time
find a positive number x such that f(x-1), f(x-2), … are negative and f(x+1), f(x+2), … are positive

Algorithm Exponential Search(lin+bin) - O(log n)
input: monotonically increasing function f(x)
output: first occurence of positive x

"""


def binary_search_exp(list, low, high, target):
    if low > high:
        return None

    while low < high:
        mid = (low + high) // 2
        if list[mid] == target:
            return target
        elif list[mid] < target:
            return binary_search_exp(list, mid + 1, high, target)
        else:
            return binary_search_exp(list, low, mid - 1, target)
    return None


# finds the range where x might exist
def exponentialSearch(list, target):
    # high, our upper bound
    h = 1
    while h < len(list) and list[h] < target:
        # keep doubling until we hit or exceed our target
        h = h * 2
    return binary_search_exp(list, h // 2, min(h, len(list) - 1), target)


a = [2, 5, 6, 8, 9, 10]
key = 9

index = exponentialSearch(a, key)

if index != -1:
    print("Element found at index", index)
else:
    print("Element found not in the list")
