"""
LeetCode 0258 - Add Digits

Difficulty: Easy

Pattern:
- Digit Processing
- Iterative Simulation

Topics (LeetCode):
- Math
- Simulation
- Number Theory

Time Complexity: O(log n)

Auxiliary Space Complexity: O(1)

Complexity Explanation:
Each iteration processes the digits of the current number using
modulo and integer division.

The number of digits in the input is proportional to log n, and
the repeated digit sums rapidly reduce the number.

Therefore, the overall time complexity is O(log n).

Only a fixed number of variables and a fixed-size set are used,
so the auxiliary space complexity is O(1).

Date Solved: 2026-09-08

Notes:
Repeatedly extracts and sums the digits of the number using modulo
and integer division until a single-digit result is obtained.
The zero case is handled separately.
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        if num == 0:
            return 0

        total = 0

        while total not in s:
            total = 0

            while num != 0:
                remainder = num % 10
                total += remainder
                num //= 10

            num = total

        return total