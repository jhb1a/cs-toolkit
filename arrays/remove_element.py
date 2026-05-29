"""
Remove Element - Two Pointers

Idea:
    Use two pointers: one to iterate through every element,
    one to track where the next valid element should be placed.
    When a non-val element is found, place it at the k pointer and advance k.
Complexity:
    Time: O(n) where n is the length of the array
    Space: O(1) - modified in place
Returns:
    int: The number of elements in nums not equal to val,
    with those elements occupying the first k positions of nums
Example:
    >>> remove_element([3,2,2,3], 3)
    2  # nums = [2,2,_,_]
    >>> remove_element([0,1,2,2,3,0,4,2], 2)
    5  # nums = [0,1,4,0,3,_,_,_]
"""


def remove_element(nums: list[int], val: int) -> int | None:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
