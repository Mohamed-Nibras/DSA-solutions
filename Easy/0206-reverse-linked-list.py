"""
LeetCode 0206 - Reverse Linked List

Difficulty: Easy

Pattern:
- Linked List Reversal
- Previous / Current / Next References

Topics (LeetCode):
- Linked List
- Recursion

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
Date Solved: 2026-09-29
Last Reinforced: N/A

Notes:
Reverse the linked list in-place by maintaining previous and current
references. Before reversing the current node's next pointer, save the
original next node to avoid losing access to the remaining list.

Core Pattern:
SAVE → REVERSE → MOVE → MOVE

next_node = current.next
current.next = previous
previous = current
current = next_node

The existing nodes are reused and their next references are reversed.
After the traversal, previous becomes the new head.

Reinforcement:
This problem was previously learned during Track 1 Phase 2 Day 26
Linked List Problem-Solving. It was reopened and independently
reconstructed before being submitted as a LeetCode solution.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head
        previous = None

        while current != None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous