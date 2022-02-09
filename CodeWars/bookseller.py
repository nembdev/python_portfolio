# A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. The 1st character of a code is a capital letter which defines the book category.

# In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

# your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.
# (A : 20) - (B : 114) - (C : 50) - (W : 0)

L1 = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}
L2 = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
cat = ["A", "B"]


def stock_list(listOfArt, listOfCat):

    # empty check
    if listOfArt == [] or listOfCat == []:
        return ""

    # combined string to be returned
    final_string = ""

    # input can be a list or a set
    # if set, convert to list and sort
    if type(listOfArt) is set:
        listOfArt = sorted(list(listOfArt))
        # print(listOfArt)
    else:
        listOfArt = sorted(listOfArt)

    # holds found categories and amounts
    matches = {}

    # if code is found, store code and amount as k:v
    for code in listOfArt:
        if code[0] in listOfCat:
            if code[0] in matches.keys():
                matches[code[0]] += int(
                    code.split(" ")[1]
                )  # split at space, convert to int
            else:
                matches[code[0]] = int(code.split(" ")[1])

    # append to final string, in order
    for category in listOfCat:
        if category in matches.keys():
            # print(f"category {category} code{category} amount{matches[category]}")
            if final_string:
                final_string += f" - ({category} : {matches[category]})"
            else:
                final_string = f"({category} : {matches[category]})"
        else:
            if final_string:
                final_string += f" - ({category} : {0})"
            else:
                final_string = f"({category} : {0})"

    # print(final_string)
    return final_string
