"""
LeetCode 905 - Sort Array By Parity

Difficulty: Easy

Pattern:
- Two Pointers
- In-Place Swapping

Topics (LeetCode):
- Array
- Two Pointers

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)

Date Solved: 2026-11-09
Last Reinforced: N/A

Notes:
- Use two pointers to move even numbers to the beginning.
- Swap each encountered even number into the next available even position.
- Both pointers start at index 0.
"""


class Solution(object):
    def sortArrayByParity(self, nums):
        even = 0
        odd = 0

        while even < len(nums):
            if nums[even] % 2 == 0:
                nums[even], nums[odd] = nums[odd], nums[even]
                odd += 1
                even += 1
            else:
                even += 1

        return nums