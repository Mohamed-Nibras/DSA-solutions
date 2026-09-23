"""
LeetCode 0977 - Squares of a Sorted Array

Difficulty: Easy

Pattern:
- Two Pointers

Topics (LeetCode):
- Array
- Two Pointers
- Sorting

Time Complexity: O(n log n)
Auxiliary Space Complexity: O(n)
Date Solved: 2026-09-23
Last Reinforced: N/A

Notes:
Initial solution squares every element and sorts the result. After solving,
an O(n) two-pointer optimization was studied using the sorted input property.
The original solution is preserved below to accurately document the solving
process and progression.

Optimization Learned:
Since the input is already sorted, the largest square must come from either
end of the array. Compare absolute values from both ends and fill a result
array from right to left, reducing the time complexity from O(n log n) to O(n).
"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        square = []

        for i in nums:
            square.append(i * i)

        return sorted(square)


# Optimization learned after the original solution:
#
# class Solution(object):
#     def sortedSquares(self, nums):
#         left = 0
#         right = len(nums) - 1
#         result = [0] * len(nums)
#
#         for i in range(len(nums) - 1, -1, -1):
#             if abs(nums[left]) > abs(nums[right]):
#                 result[i] = nums[left] * nums[left]
#                 left += 1
#             else:
#                 result[i] = nums[right] * nums[right]
#                 right -= 1
#
#         return result