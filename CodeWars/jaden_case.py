# takes a string and capitalizes the first letter in each word 
def to_jaden_case(string):
    
    # splits the string
    # loops through the list
    # runs capitalize on each item
    # joins the now capital words
    return " ".join( set.capitalize() for set in string.split())
