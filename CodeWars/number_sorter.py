# original
# takes a number, reverse sorts it, returns it
def descending_order(num):
    # converts to a string, then reverse sorts
    str_nums = sorted(str(num), reverse=True)

    # joins the list, converts back to a number
    return int("".join(str_nums))


# check
print(descending_order(48720502))

# could be one line
return int("".join(sorted(str(num), reverse=True)))
