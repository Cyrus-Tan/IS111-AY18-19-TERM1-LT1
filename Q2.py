def represent_numbers(start, end):
    output_string = ''                          # create empty string
    if end < start:
        return output_string                    # returns empty string
    else:
        for num in range(start, end + 1):       # add 1 because end is not inclusive
            output_string += abs(num)*'-'            # multiply '-' by abs(num)
            if num < end:
                output_string += '#'            # add '#' between integers, only if haven't reach final num
        return output_string


#print(represent_numbers(1, 5))
#print(represent_numbers(3, 5))
#print(represent_numbers(-3, 1))
#print(represent_numbers(1, 1))
#print('[' + represent_numbers(3, 1) + ']')