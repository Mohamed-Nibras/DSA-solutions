"""
LeetCode 0771 - Jewels and Stones

Difficulty: Easy

Pattern:
- Set
- Set Membership Checking

Topics (LeetCode):
- Hash Table
- String

Time Complexity: O(j + s)

Auxiliary Space Complexity: O(j)

Date Solved: 2026-08-02
Last Reinforced: N/A

Notes:
Stores the jewel types in a set and traverses the stones, incrementing
the count whenever the current stone exists in the jewel set.
"""


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """

        jewel_set = set(jewels)
        count = 0

        for stone in stones:
            if stone in jewel_set:
                count += 1

        return count