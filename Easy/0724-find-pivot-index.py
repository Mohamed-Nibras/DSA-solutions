"""
LeetCode 0724 - Find Pivot Index

Difficulty: Easy

Pattern:
- Running Sum
- Prefix Sum

Topics (LeetCode):
- Array
- Prefix Sum

Time Complexity: O(n)

Auxiliary Space Complexity: O(1)

Complexity Explanation:
Calculating the initial total sum requires O(n) time, and the following
single traversal also requires O(n) time. Since these operations occur
sequentially, the overall time complexity remains O(n).

Only a constant number of scalar variables are maintained regardless of
the size of nums. Although left_sum and right_sum contain values derived
from the input, the amount of additional storage does not grow with the
number of elements. Therefore, the auxiliary space complexity is O(1).

Date Solved: 2026-08-04
Last Reinforced: N/A

Notes:
Maintains the sum strictly to the left and right of each index. Before
checking an index, removes the current element from right_sum so the pivot
belongs to neither side. If both sums are equal, that index is returned;
otherwise, the current element joins left_sum for the next iteration.

Prior Exposure:
Previously encountered during Semester 2 Phase 1 subject practice but was
not documented in the DSA repository. The running-total optimization was
remembered, while the implementation was reconstructed during this solve.
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1