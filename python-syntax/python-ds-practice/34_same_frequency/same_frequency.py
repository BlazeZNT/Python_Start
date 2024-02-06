def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    # print(str1)
    # for i in str1:
    #     if str1.count(i) == str2.count(i):
    #         return True
    #     else:
    #         return False
    return all(True if str1.count(char) == str2.count(char) else False for char in str1)
        
print(same_frequency(321142, 3212215))
