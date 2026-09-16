"""
LeetCode 1512 - Number of Good Pairs

Difficulty: Easy

Pattern:
- Frequency Counting
- Hash Map

Topics (LeetCode):
- Array
- Hash Table
- Math
- Counting

Time Complexity: O(n)

Auxiliary Space Complexity: O(n)

Date Solved: 2026-09-16
Last Reinforced: N/A

Notes:
For each number, its previous frequency directly represents the number of
new good pairs formed with the current occurrence.
"""


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        pair = 0

        for i in nums:
            if i in freq:
                pair += freq[i]
            freq[i] = freq.get(i, 0) + 1

        return pair