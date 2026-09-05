"""
LeetCode 0657 - Robot Return to Origin

Difficulty: Easy

Pattern:
- Coordinate Tracking
- Simulation
- Two-Dimensional Movement

Topics (LeetCode):
- String
- Simulation

Time Complexity: O(n)

Auxiliary Space Complexity: O(1)

Complexity Explanation:
The moves string is traversed once, and each movement updates one
of the two coordinate variables.

Each move takes constant time to process, so the overall time
complexity is O(n), where n is the number of moves.

Only the x and y coordinates are stored regardless of the number
of moves, so the auxiliary space complexity is O(1).

Date Solved: 2026-09-05
Last Reinforced: N/A

Notes:
Tracks horizontal and vertical movement separately using x and y
coordinates. The robot returns to the origin only when both
coordinates are 0.
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0

        for i in moves:
            if i == "R":
                x += 1
            if i == "L":
                x -= 1
            if i == "U":
                y += 1
            if i == "D":
                y -= 1

        return (x == 0) & (y == 0)