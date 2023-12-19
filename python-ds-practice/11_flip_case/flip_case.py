def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    #list comprehension to swap  the case of a character 
    flipped_phrase = [char.swapcase() if char.lower() == to_swap.lower() else char for char in phrase]
    return ''.join(flipped_phrase)