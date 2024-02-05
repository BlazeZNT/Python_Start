def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

            >>> flip_case('Aaaahhh', 'a')
            'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    
    new_word = ""
    for word in phrase:
        if (word == to_swap.lower()):
            new_word += word.upper()
        elif(word == to_swap.upper()):
            new_word += word.lower()
        else:
            new_word += word
            
    return new_word

print(flip_case('Aaaahhh', 'h'))