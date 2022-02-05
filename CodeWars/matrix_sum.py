#sum all values in a given matrix
def matrix_sum(matrix):
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            total += matrix[row][col]

    print(total)
