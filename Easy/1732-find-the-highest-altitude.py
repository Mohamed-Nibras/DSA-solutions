"""
LeetCode 1732 - Find the Highest Altitude

Difficulty: Easy

Pattern:
- Prefix Sum
- Running Sum

Topics (LeetCode):
- Array
- Prefix Sum

Time Complexity: O(n)
Auxiliary Space Complexity: O(n)

Date Solved: 2026-11-10
Last Reinforced: N/A

Notes:
- Start with an initial altitude of 0.
- Accumulate each gain to calculate the next altitude.
- Return the maximum altitude reached.
"""


class Solution(object):
    def largestAltitude(self, gain):
        result = [0]

        for i in range(len(gain)):
            result.append(result[-1] + gain[i])

        return max(result)