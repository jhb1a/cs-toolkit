"""
Valid parentheses - Stack

Idea:
    Use a stack to track unmatched opening brackets.
    When a closing bracket is encountered, check if it matches
    the most recently seen opening bracket (top of stack).
    At the end, the stack should be empty if all brackets matched.

Complexity:
    Time: O(n) where n is the length of the string
    Space: O(n) in the worst case where all characters are opening brackets

Returns:
    bool: True if the string is valid, False otherwise

Example:
    >>> valid_parentheses("([])")
    True
    >>> valid_parentheses("(]")
    False
    >>> valid_parentheses("([)")
    False
"""


def valid_parentheses(s: str) -> bool | str:
    matching = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in s:
        if char in matching:
            # closing bracket
            if not stack:
                return False
            top = stack.pop()
            if top != matching[char]:
                return False
        else:
            # open bracket
            stack.append(char)
    return not stack
