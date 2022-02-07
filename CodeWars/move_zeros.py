def move_zeros(array):

    zero_count = 0
    new_array = []
    for i in range(len(array)):
        print(i)
        if array[i] == 0:
            zero_count += 1
        else:
            new_array.append(array[i])

    for i in range(zero_count):
        new_array.append(0)

    return new_array


# a = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]

# print(move_zeros(a))
