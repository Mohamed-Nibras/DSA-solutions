
"""
LeetCode 414 - Third Maximum Number

Difficulty: Easy

Pattern:
- Remove Duplicates
- Sorting

Topics (LeetCode):
- Array
- Sorting

Time Complexity: O(n log n)
Auxiliary Space Complexity: O(n)

Date Solved: 2026-11-05
Last Reinforced: N/A

Notes:
- Use a set to remove duplicate values before sorting.
- Return the third-largest distinct value if at least three distinct
  values exist; otherwise, return the maximum value.
"""


class Solution(object):
    def thirdMax(self, nums):
        array = set(nums)

        if len(array) > 2:
            array = sorted(array, reverse=True)
            return array[2]
        else:
            array = sorted(array, reverse=True)
            return array[0]