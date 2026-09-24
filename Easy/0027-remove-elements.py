"""
LeetCode 0027 - Remove Element

Difficulty: Easy

Pattern:
- Two Pointers / Write Pointer

Topics (LeetCode):
- Array
- Two Pointers

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
Date Solved: 2026-09-24
Last Reinforced: N/A

Notes:
Use a read pointer to scan the array and a write pointer to place each
non-target element at the next valid position. The final write pointer
value represents the number of remaining elements.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        left = 0
        right = 0

        while right < len(nums):

            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
                right += 1

            else:
                right += 1

        return left