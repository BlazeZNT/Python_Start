def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    return not any(not isinstance(i,list) for i in lst)


print(list_check([[1], "nope"]))