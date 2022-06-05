def print_dancing_string(sentence, start):
    length_sentence = len(sentence)         # get length of the string
    a = [[" " for x in range(length_sentence)] for y in range(length_sentence)]  # create 2d character array
    # for counting the rows in zig-zag
    row = 0
    for char in range(length_sentence):
        a[row][char] = sentence[char]       # put characters in the matrix
        if row == n-1:


#print_dancing_string('a', 'T')
print_dancing_string('abcdefghi', 'T')

# LEFTOVER ISSUE: Can't continue
# check--> https://www.geeksforgeeks.org/print-string-wave-pattern/
#      --> https://stackoverflow.com/questions/52766301/printing-a-w-pattern-with-alphabets-abcdefghi-for-python