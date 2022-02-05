"""
Given a CSV file and the name of a column, outputs the index (starting at 0) of that column
"""
from csv import reader

# Test Inputs
csv_filename = ""
col_name1 = "test"
col_name2 = "random"  # returns -1 if not found


def find_col_index(file, col_name):
    # load the csv file and store it in a list
    data = list(reader(open(file)))

    # searches for the named value, returns the index
    try:
        return data[0].index(col_name)
    # if its not found return -1
    except ValueError:
        return -1


# example
find_col_index(csv_filename, col_name1)
