def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_list = phrase.split()
    finish_list = []
    for word in new_list:
        new_word = word.lower()
        divide = list(new_word)
        divide[0] = divide[0].upper()
        modified = ''.join(divide)
        finish_list.append(modified)
        
        
    finish_list = " ".join(finish_list)
    return finish_list
    

print(titleize('this is awesome'))