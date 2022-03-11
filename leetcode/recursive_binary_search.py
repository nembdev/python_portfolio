# takes a sorted list, returns true or false if target exists
# with each search, the list is halved
def recursive_binary_search(list, target):
    # passed in empty list
    if len(list) == 0:
        return False
    else:
        # midpoint = half the length of list
        midpoint = len(list) // 2  # floor

    if list[midpoint] == target:
        return True
    else:
        if list[midpoint] < target:
            # recursive + slice
            # create a new list with start/end points
            return recursive_binary_search(list[midpoint + 1 :], target)  # : to the end
        else:
            return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target Found: ", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 7)
verify(result)

result = recursive_binary_search(numbers, 66)
verify(result)
