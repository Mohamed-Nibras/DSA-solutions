"""
LeetCode 0876 - Middle of the Linked List

Difficulty: Easy

Pattern:
- Fast & Slow Pointers
- Linked List Traversal

Topics (LeetCode):
- Linked List
- Two Pointers

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
Date Solved: 2026-10-01
Last Reinforced: N/A

Notes:
Use two pointers starting at the head. The slow pointer moves one node at
a time while the fast pointer moves two nodes at a time. When fast reaches
the end of the linked list, slow points to the middle node.

For an even-length linked list, this naturally returns the second middle
node because fast advances two nodes per iteration.

Core Pattern:
slow → 1 step
fast → 2 steps

Loop Condition:
fast is not None and fast.next is not None

Reinforcement:
This problem was previously learned during Track 1 Phase 2 Day 26
Linked List Problem-Solving. It was reopened and reconstructed as a
LeetCode solution before being submitted and accepted.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow