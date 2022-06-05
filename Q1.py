def get_color(code):
    """returns a string that is either 'Red', 'Green', 'Blue' or 'Invalid'"""
    code_updated = code.lower()         # convert code to lower case
    if code_updated == "r":
        return "Red"
    elif code_updated == "g":
        return "Green"
    elif code_updated == 'b':
        return "Blue"
    else:
        return "Invalid"


#print(get_color('r'))
#print(get_color('G'))
#print(get_color('Blue Sky'))
#print(get_color(''))