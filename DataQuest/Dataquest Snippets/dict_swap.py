def swap(a_dict):
    """
    swaps the keys/values in a given dictionary
    """
    keys = []
    values = []
    new_dict = {}
    for key in a_dict:
        keys.append(key)
        values.append(a_dict[key])

    for i in range(len(values)):
        new_dict[values[i]] = keys[i]

    return new_dict
