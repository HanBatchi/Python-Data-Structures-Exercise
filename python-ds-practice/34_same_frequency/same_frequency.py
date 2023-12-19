def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str_num1, str_num2 = str(num1) , str(num2)

    if len(str_num1) != len(str_num2):
        return False
    
    # Count occurrences of each digit in both numbers
    count_num1 = {digit: str_num1.count(digit) for digit in set(str_num1)}
    count_num2 = {digit: str_num2.count(digit) for digit in set(str_num2)}

    # Compare the dictionaries
    return count_num1 == count_num2