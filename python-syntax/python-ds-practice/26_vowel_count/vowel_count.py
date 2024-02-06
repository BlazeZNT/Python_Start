def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels_Dict = {}
    vowels = "aeiou"
    for char in phrase:
        if char.lower() in vowels:
            if (char.lower() in vowels_Dict):
                vowels_Dict[char.lower()] += 1
            else:
                vowels_Dict[char.lower()] = 1
    return vowels_Dict

print(vowel_count('HOW ARE YOU? i am great!') )

        