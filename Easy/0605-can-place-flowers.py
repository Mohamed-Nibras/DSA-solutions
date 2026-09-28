"""
LeetCode 0605 - Can Place Flowers

Difficulty: Easy

Pattern:
- Greedy / Local Placement
- Array Simulation

Topics (LeetCode):
- Array
- Greedy

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
Date Solved: 2026-09-28
Last Reinforced: N/A

Notes:
Scan the flowerbed from left to right and plant a flower whenever the
current position and all of its existing adjacent positions are empty.
The flowerbed is modified in-place, and n is reduced after each valid
placement. Boundary positions and the single-element flowerbed require
separate handling because they do not have two neighbors.

Learning:
This problem required careful handling of boundary positions and edge
cases. The solution was developed through several iterations, beginning
with checking only middle positions, then adding explicit handling for
the first and last positions and finally the single-element case.
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return True

        if len(flowerbed) == 1 and flowerbed[0] == 1 and n != 0:
            return False

        elif len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True

        for i in range(len(flowerbed)):

            if n == 0:
                return True

            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

        return n == 0