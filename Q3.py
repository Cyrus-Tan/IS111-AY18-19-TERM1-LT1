def mask_out(sentence, banned, substitutes):
    list_of_banned = list(banned)                           # convert string to list of individual char
    list_of_substitutes = list(substitutes)
    new_sentence = ''
    for letter in sentence:                                 # check if letter is banned
        if letter not in list_of_banned:                    # add letter to empty string if not banned
            new_sentence += letter
        else:                                                       # if letter is banned
            index_banned = list_of_banned.index(letter)             # find index of banned char in banned list
            if index_banned > len(list_of_substitutes) - 1:         # if there's additional chars in banned list
                substituted_letter = list_of_substitutes[0]         # additional chars in banned will be replaced by first char in substitutes
                new_sentence += substituted_letter
            else:
                substituted_letter = list_of_substitutes[index_banned]  # get the substitute char
                new_sentence += substituted_letter
    return new_sentence


#print(mask_out('pineapple', 'e', '#'))
#print(mask_out('pineapple', 'aeiou', '#$%^&'))
#print(mask_out('pineapple', 'aeiou', '#$'))