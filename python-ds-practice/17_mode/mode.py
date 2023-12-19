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
    #we create a dictionary to store the count number of items
    num_counts = {}
    #we iterate to count the ocurrances of each number
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) +1
    #to find the most common number in the count
    most_commom_count = max(num_counts, key = num_counts.get)
    
    return most_commom_count