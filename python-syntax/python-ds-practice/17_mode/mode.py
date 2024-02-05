def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    og_num = 0
    total_num = 0
    for num in nums:
        if (nums.count(num)>total_num):
            total_num = nums.count(num)
            og_num = num
    return og_num

print (mode([1, 2, 1]))

