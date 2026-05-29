"""
Plus One - Reverse Iteration

Idea:
    Iterate backwards through the digits. If the current digit is less than 9,
    increment it and return immediately. Otherwise set it to 0 and carry.
    If all digits were 9, prepend 1 to the list.
Complexity:
    Time: O(n) where n is the number of digits
    Space: O(1) modified in place, except the all-nines edge case which is O(n)
Returns:
    list[int]: The digits array incremented by one
Example:
    >>> plus_one([1,2,3])
    [1,2,4]
    >>> plus_one([9,9,9])
    [1,0,0,0]
"""


def plus_one(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
