class MyClass:

    # sets data attribute to list argument
    def __init__(self, a_list):
        self.data = a_list

    # appends a value to data attribute*
    def append(self, new_data):
        # converts argument to a single item list
        new_data = [new_data]
        #adds the new list to the end of the data attribute
        self.data += new_data


example = MyClass([1, 2, 3, 4, 5])
example.append(6)

print(my_list.data)


# One line Version
# self.data += [new_data]
