"""
LeetCode 704 - Binary Search

Difficulty: Easy

Pattern:
- Binary Search

Topics (LeetCode):
- Array
- Binary Search

Time Complexity: O(log n)

Auxiliary Space Complexity: O(1)

Date Solved: 2026-09-20
Last Reinforced: N/A

Notes:
Use two boundary indices to repeatedly divide the sorted search range in half.
If the target is smaller than the middle element, search the left half; if it
is larger, search the right half. Return the middle index when the target is
found, otherwise return -1.
"""


class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid - 1

            elif target > nums[mid]:
                left = mid + 1

            else:
                return mid

        return -1