"""
LeetCode 0485 - Max Consecutive Ones

Difficulty: Easy

Pattern:
- Consecutive Sequence Tracking
- Running Count
- Maximum So Far

Topics (LeetCode):
- Array

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
Date Solved: 2026-10-03
Last Reinforced: N/A

Notes:
Traverse the binary array while maintaining the current consecutive count
of 1s and the maximum count seen so far. When a 0 is encountered, reset
the current count because the consecutive sequence has ended.

Core Pattern:
1 → INCREMENT CURRENT COUNT
0 → RESET CURRENT COUNT
TRACK MAXIMUM

The current count represents the active streak, while max_count preserves
the best streak found during the traversal.
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0

        for i in nums:
            if i == 1:
                count += 1
                if count > max_count:
                    max_count = count

            else:
                if count > max_count:
                    max_count = count
                count = 0

        return max_count