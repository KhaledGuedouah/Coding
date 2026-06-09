# Interview preparation practice module.
# Contains singly linked list interview algorithms.

from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


def to_list(head: ListNode | None) -> list[int]:
    values: list[int] = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def reverse_iterative(head: ListNode | None) -> ListNode | None:
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def reverse_recursive(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n):
        if not fast.next:
            return head
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next if slow.next else None
    return dummy.next


def has_cycle(head: ListNode | None) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def middle_node(head: ListNode | None) -> ListNode | None:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_two_sorted_lists(head1: ListNode | None, head2: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    p1, p2 = head1, head2

    while p1 and p2:
        if p1.val <= p2.val:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    tail.next = p1 if p1 else p2
    return dummy.next


def sort_list(head: ListNode | None) -> ListNode | None:
    # Merge sort on linked list: O(n log n) time, O(log n) recursion stack.
    if not head or not head.next:
        return head

    prev = None
    slow = fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None
    left = sort_list(head)
    right = sort_list(slow)
    return merge_two_sorted_lists(left, right)


if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    sorted_head = sort_list(head)
    assert to_list(sorted_head) == [1, 2, 3, 4]
    assert to_list(reverse_iterative(sorted_head)) == [4, 3, 2, 1]
