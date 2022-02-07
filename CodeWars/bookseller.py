# A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. The 1st character of a code is a capital letter which defines the book category.

# In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

# your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.
# (A : 20) - (B : 114) - (C : 50) - (W : 0)

L1 = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}
L2 = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
cat = ["A", "B"]


def stock_list(listOfArt, listOfCat):
    final_string = ""
    for letter in listOfCat:
        cat_amount = 0
        for code in listOfArt:
            if code[0] == letter:
                cat_amount += int(code[6:])
        if final_string:
            final_string += f" - ({letter} : {cat_amount})"
        else:
            final_string += f"({letter} : {cat_amount})"
    return final_string


stock_list(L1, cat)
