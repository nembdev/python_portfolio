# A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. The 1st character of a code is a capital letter which defines the book category.

# In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

# your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.
# (A : 20) - (B : 114) - (C : 50) - (W : 0)

L1 = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}
L2 = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
cat = ["A", "B"]


def stock_list(listOfArt, listOfCat):
    # combined string to be returned
    final_string = ""
    # holds the total for each category and the letter code
    cat_amount = {}

    # check for type, either list or set
    # if set, concert to list and sort
    if type(listOfArt) is set:
        listOfArt = sorted(list(listOfArt))
        # print(listOfArt)

    # loop through each code
    for code in listOfArt:
        # print(code)
        # first index is the letter code
        # if found increase cat_amount
        if code[0] in listOfCat:
            # key is the letter, amount is index 6:, converted to an int
            # print(cat_amount)
            if code[0] in cat_amount.keys():
                cat_amount[code[0]] += int(code[6:])
            else:
                cat_amount[code[0]] = int(code[6:])

    for key in cat_amount:
        if final_string:
            final_string += f" - ({key} : {cat_amount[key]})"
        else:
            final_string += f" ({key} : {cat_amount[key]})"

    return final_string


stock_list(L1, cat)
