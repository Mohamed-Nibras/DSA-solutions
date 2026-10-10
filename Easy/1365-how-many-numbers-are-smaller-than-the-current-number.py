"""
LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number

Difficulty: Easy

Pattern:
- Brute Force
- Nested Loop Traversal
- Counting

Topics (LeetCode):
- Array
- Hash Table
- Sorting
- Counting Sort

Time Complexity: O(n^2)
Auxiliary Space Complexity: O(n)

Date Solved: 2026-10-09
Last Reinforced: N/A

Notes:
- For each element, traverse the entire array and identify all elements
  that are strictly smaller than the current element.
- Store the smaller elements in a temporary list and append the list's
  length to the result.
- Initialize the temporary list once per outer-loop iteration so that
  the count accumulates across all inner-loop comparisons.
- An initial implementation incorrectly reset the temporary list during
  every inner-loop iteration. This was corrected by moving its
  initialization into the outer loop.
- Solved independently using a brute-force approach and accepted after
  correcting the initialization scope.
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums)):
            current = []
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    current.append(nums[j])

            result.append(len(current))

        return result