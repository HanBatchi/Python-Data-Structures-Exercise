def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """ 
    #We extract the hobbies of each friend
    hobbie_a = set(a[2])
    hobbie_b = set(b[2])
    #Check if they have common hobbies
    common_hobbies = hobbie_a.intersection(hobbie_b)
    # Return True if there are common hobbies, False otherwise
    return bool(common_hobbies)