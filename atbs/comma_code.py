def comma_code(a_list):
    """
    takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item
    """
    result = ""

    if not a_list:
        print("please provide a non empty list")
        return

    for val in a_list:
        if val == a_list[-1]:
            result += "and " + val
        else:
            result += val + ", "

    print(result)


test_vals = ["apples", "bananas", "tofu", "cats"]
test_vals2 = []

comma_code(test_vals)
comma_code(test_vals2)
