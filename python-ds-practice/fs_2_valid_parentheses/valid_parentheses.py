def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    stack  = []
    parentheses_map = {')' : '(', '{': '}', ']':'['}
    for char in parens:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if stack and stack[-1] == parentheses_map[char]:
                stack.pop()
            else:
                return False
            
    return not stack
