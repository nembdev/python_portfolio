def filter(a_list):
    """
    a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
    """
    filtered = []

    for item in a_list:
        if type(item) != str:
            filtered.append(item)
    return filtered


def filter_short(a_list):
    """
    fancy one line
    """
    return [item for item in a_list if type(item) != str]
