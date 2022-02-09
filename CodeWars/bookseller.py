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

    # letter_code: category amount
    cat_amount = {}

    # input can be a list or a set
    # if set, convert to list and sort
    if type(listOfArt) is set:
        listOfArt = sorted(list(listOfArt))
        # print(listOfArt)
    else:
        listOfArt = sorted(listOfArt)
        listOfCat = sorted(listOfCat)

    for i in range(len(listOfCat)):
        if i < len(listOfArt):
            code = listOfArt[i][0]
            amount = listOfArt[i].split(" ")[1]
            # print(i)
            # print(code)
            if code in listOfCat:
                if code in cat_amount.keys():
                    cat_amount[code] += int(amount)
                else:
                    cat_amount[code] = int(amount)
        if listOfCat[i] not in cat_amount.keys():
            cat_amount[listOfCat[i]] = 0

    for key in cat_amount:
        if final_string:
            final_string += f" - ({key} : {cat_amount[key]})"
        else:
            final_string += f"({key} : {cat_amount[key]})"

    # return final_string
    print(final_string)
