#Cleaning Date Category in a sample moma dataset

#fake data similiar to our cleaning target
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

#characters we want filtered
bad_chars = ["(",")","c","C",".","s","'", " "]

#filters based on above
#returns the string
def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

#test data ran through first filter
stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

#removing -, calculating averages in a range, and converting all to ints
def process_date(string):
    if "-" in string:
        # remove the -, return a list
        # stores
        split_vals = string.split("-")

        # convert to float,store in new_list
        floats = []
        for val in split_vals:
            floats.append(int(val))

        #find the avg for a range
        avg_date = round(((floats[0] + floats[1]) / 2))

        return avg_date
    else:
        return int(string)

#empty list for final data
processed_test_data = []

#process each row
for data in stripped_test_data:
        processed_test_data.append(process_date(data))

#print to check
print(processed_test_data)

#Cleaning the Date row in our real Dataset
for row in moma:
    date = row[6]
    date = strip_characters(date)
    date = process_date(date)

    row[6] = date
