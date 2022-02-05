"""
Given the name of a column in a CSV file
outputs True if all values in that column are unique
False otherwise
Assumes find_col_index() is defined
"""
from csv import reader

# test inputs
csv_filename = ".csv"
col_name1 = ""


def check_unique_values(csv_filename, col_name):

    # returns the index of the given column
    index = find_col_index(csv_filename, col_name)

    # if not found
    if index == -1:
        return None

    # opens the file again, and removes the header
    data = list(reader(open(csv_filename)))
    data = data[1:]

    uniqs = {}

    # sorts and builds a freq table
    for i in range(len(data) - 1):

        val = data[i][index]

        # print(val) to check output
        if val not in uniqs:
            uniqs[val] = 1
        else:
            uniqs[val] += 1

    # very simple yes or no
    for value in uniq:
        if uniq[value] > 1:
            return False

    return True
