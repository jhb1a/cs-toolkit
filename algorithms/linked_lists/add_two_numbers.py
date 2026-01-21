"""
Add two non-negative integers represented as reversed linked lists.

Idea:
    Each node contains a single digit, and the result is constructed by
    summing corresponding digits with carry propagation. Traversal continues
    until both lists are exhausted and no carry remains.

Complexity:
    Time: O(n) - each list is traversed once
    Space: O(n) - result digits are accumulated before list construction

Returns:
    Head of a new linked list representing the sum in the same reversed format.
"""

from typing import Optional

from data_structures.linked_lists import ListNode, build_list


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    result_array = []

    while l1 or l2 or carry:
        # Case-handling for None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum = val1 + val2 + carry
        carry = 0

        # Carry the 1
        if sum > 9:
            sum -= 10
            carry = 1

        result_array.append(sum)

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return build_list(result_array)


if __name__ == "__main__":
    # Test inputs
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])

    result = add_two_numbers(l1, l2)
