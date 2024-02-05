def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    
    new_phrase = list(phrase)
    new_phrase[0] = new_phrase[0].upper()
    og = ''.join(new_phrase)
    return og

    

    
print(capitalize("hello"))