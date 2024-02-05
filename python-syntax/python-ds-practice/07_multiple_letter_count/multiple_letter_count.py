def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    new_list = {}
   
    for word in phrase: 
        if (new_list.get(word) == None):
            new_list[word] = 1;
        else:
            new_list[word] +=1;
            

    return new_list
        
        



print(multiple_letter_count("tiger"))