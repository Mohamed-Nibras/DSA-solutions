"""
LeetCode 0136 - Single Number

Difficulty: Easy

Pattern:
- Bit Manipulation
- XOR

Topics (LeetCode):
- Array
- Bit Manipulation

Time Complexity: O(n)

Auxiliary Space Complexity: O(1)

Date Solved: 2026-08-31
Last Reinforced: N/A

Notes:
Uses XOR to cancel every element that appears twice, because XORing
a value with itself produces 0 and XORing any value with 0 preserves
that value. Therefore, after all pairs cancel out, only the element
appearing exactly once remains.

Complexity Explanation:
The array is traversed exactly once, so the time complexity is O(n).

Only one accumulator variable is used regardless of the number of
elements in the input, so the auxiliary space complexity is O(1).
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0

        for num in nums:
            result ^= num

        return result