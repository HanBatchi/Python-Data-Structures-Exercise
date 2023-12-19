def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    words = phrase.split()
    #it separates words in the list, in this case, separates the first word to capitalize it, and then it add the rest of the words
    capitalized_phrase = ' '.join([words[0].capitalize()] + words[1:])
    
    return capitalized_phrase
        
         