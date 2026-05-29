from typing import Optional

from .linked_lists import ListNode, build_list, print_list


# TODO: Finish iterating
def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    print_list(head)


# Test
head = build_list([1, 1, 2, 3, 3])
print_list(delete_duplicates(head))
