"""
LeetCode 0238 - Product of Array Except Self

Difficulty: Medium

Pattern:
- Prefix Product
- Suffix Product

Topics (LeetCode):
- Array
- Prefix Sum

Time Complexity: O(n)
Auxiliary Space Complexity: O(n)
Date Solved: 2026-11-11
Last Reinforced: N/A

Notes:
Initial solution used brute force with two nested loops to calculate the
product of all elements except the current index. Although logically correct,
it resulted in TLE due to O(n²) time complexity.

The optimized solution calculates cumulative products from the left and
right using two separate passes. The right-product list is reversed and
combined with the left-product list using zip() to obtain the final answer.

Optimization Learned:
Instead of recalculating the product for every index, maintain cumulative
products from both directions. Each element's answer is obtained by
multiplying the product of all elements to its left with the product of
all elements to its right, achieving O(n) time complexity.
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result_l = []
        result_r = []
        left_product = 1
        right_product = 1

        for i in range(len(nums)):
            result_l.append(left_product)
            left_product *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            result_r.append(right_product)
            right_product *= nums[i]

        return [i * j for i, j in zip(result_l, reversed(result_r))]


# Optimization learned after the original solution:
#
# class Solution(object):
#     def productExceptSelf(self, nums):
#         result = [1] * len(nums)
#
#         left_product = 1
#         for i in range(len(nums)):
#             result[i] = left_product
#             left_product *= nums[i]
#
#         right_product = 1
#         for i in range(len(nums) - 1, -1, -1):
#             result[i] *= right_product
#             right_product *= nums[i]
#
#         return result