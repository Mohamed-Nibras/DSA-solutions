"""
LeetCode 509 - Fibonacci Number

Difficulty: Easy

Pattern:
- Iterative Dynamic Programming
- State Tracking

Topics (LeetCode):
- Math
- Dynamic Programming
- Recursion
- Memoization

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)

Date Solved: 2026-11-10
Last Reinforced: N/A

Notes:
- Maintain the previous two Fibonacci numbers.
- Calculate the next number by adding them.
- Update both previous values during each iteration.
"""


class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0

        if n == 1:
            return 1

        first = 0
        second = 1

        for number in range(2, n + 1):
            next = first + second
            first = second
            second = next

        return second

        # first = n - 1
        # second = n - 2

        # return self.fib(first) + self.fib(second)