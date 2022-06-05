def expand(text):
    updated_string = ""                  # will be where i index the replacement letters
    final_string = ""
    start_number_as_string = ""
    end_number_as_string = ""
    start_number_as_int = 0
    end_number_as_int = 0
    for char in text:
        if char.isalpha() == True or char == " ":          # if char is an alphabet or whitespace
            updated_string += char                         # add char to updated_string

    # To find index of all occurrences of dash - in text, append all index to a list
    all_index_of_dash = []
    for index in range(len(text)):
        if text[index] == "-":                                # if char is dash -
            index_of_dash = index
            all_index_of_dash.append(index_of_dash)           # add the index of dash to the list

    # Will start from first index
    dash_index = -1

    # if not alphabet or whitespace--> will be &, number or -
    for char in text:
        if char.isalpha() == True or char == " ":
            final_string += char                        # add char to final_string
        elif char == "-":                        # if char is dash -
            pass                                 # don't do anything
        elif char == "&":                        # if char is &, add dash_index by 1
            dash_index += 1
        else:                                    # if char is number----> will always be after ampersand &
            index_of_char = text.index(char)
            index_of_dash = all_index_of_dash[dash_index]
            if index_of_char < index_of_dash:    # if number is before dash -
                start_number_as_string += char
                start_number_as_int += int(start_number_as_string)
            elif index_of_char > index_of_dash:  # if number is after dash -
                end_number_as_string += char
                end_number_as_int += int(end_number_as_string)

                # Once i have gotten both start and end number, bottom will be run
                for index in range(start_number_as_int, end_number_as_int + 1):
                    if index > len(updated_string) - 1:
                        char_to_be_replaced = "?"                                   # ? will be shown as a char if invalid index
                    else:
                        char_to_be_replaced = updated_string[index]                 # find char to be replaced
                    final_string += char_to_be_replaced

                ### Reset the variables so that start number and end number back to 0, ready to be added on again if there's more
                start_number_as_string = ""
                end_number_as_string = ""
                start_number_as_int = 0
                end_number_as_int = 0

    return final_string


#print(expand('ABC &5-7 XYZ'))
print(expand('&0-3&4-5ABC XYZ'))
#print(expand('&2-5ABC'))
#print(expand('ABC &6-9 XYZ'))

# LEFTOVER ISSUE: Can't solve if there's more than one index references            (SOLVED)
#       ---------> How to be able to loop through as many times as there is index reference
#       ---------> E.g: How to separate/differentiate the (first & and -) with the (second & and -)
#       SOLUTION: USE for loop in range(len(text)), if text[index] == "-", then get the index and append it to a new list
#                 DONT USE (for char in text, if char == "-", then get its index) ----> because it will always only return the
#                                                                  first index of occurrence instead of all indexes