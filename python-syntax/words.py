def print_upper_words(words,wordset):
    ''' this will take in a list of strings and turn them into uppercase.'''
    for word in words:
        new_word = word.upper()
        for val in wordset:
            new_val = val.upper()
            if(new_word[0] == f"{new_val}"):
                print(new_word)
        
        
print_upper_words(["hello","hi","konichiwa","eidadakimas","gomenasai"],{"a","h","K"})