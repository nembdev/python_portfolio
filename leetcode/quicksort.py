"""
Quicksort
    divide and conquer

    find a pivot
        partitions
            hoare partition
                pivot: left most
                start: start + 1
                end: tail

                move until start is greater than pivot
                move end until less than pivot

                swap start and end
                repeat until end crosses start
                swap end with pivot
    split the list in left and right based on pivot
    sort left, then right
    merge
"""


def h_partition(list, start, end):

    pivot_index = start  # left most
    pivot = list[pivot_index]

    # until end crosses start
    while start < end:
        # move start forward until greater than pivot
        while start < len(list) and list[start] <= pivot:
            start += 1

        # move end backwards until less thna pivot
        while list[end] > pivot:
            end -= 1

        # once both are found, swap the values
        if start < end:
            list[start], list[end] = list[end], list[start]

    list[end], list[pivot_index] = list[pivot_index], list[end]

    return end


def quicksort(list, start, end):
    # base case check
    if len(list) <= 1:
        return list

    if start < end:
        partition_index = h_partition(list, start, end)

        quicksort(list, start, partition_index - 1)  # left
        quicksort(list, partition_index + 1, end)  # right

    return list


list = [11, 9, 2, 7, 29, 15, 28]

print(quicksort(list, 0, len(list) - 1))
