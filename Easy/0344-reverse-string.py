"""
LeetCode 0344 - Reverse String

Difficulty: Easy

Pattern:
- Two Pointers
- In-Place Array Modification

Topics (LeetCode):
- Two Pointers
- String

Time Complexity: O(n)

Auxiliary Space Complexity: O(1)

Date Solved: 2026-09-13
Last Reinforced: N/A

Notes:
Uses two pointers starting at opposite ends of the character array.
Swaps the characters and moves both pointers inward until they meet.
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1