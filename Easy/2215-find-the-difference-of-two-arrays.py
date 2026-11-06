"""
LeetCode 2215 - Find the Difference of Two Arrays

Difficulty: Easy

Pattern:
- Set Difference
- Set Membership

Topics (LeetCode):
- Array
- Hash Table

Time Complexity: O(n + m)
Auxiliary Space Complexity: O(n + m)

Date Solved: 2026-11-06
Last Reinforced: N/A

Notes:
- Convert both arrays into sets to eliminate duplicates.
- Use set difference to find elements exclusive to each array.
"""


class Solution(object):
    def findDifference(self, nums1, nums2):
        n1 = set(nums1)
        n2 = set(nums2)

        return list([list(n1 - n2), list(n2-n1)])