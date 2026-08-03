"""
LeetCode 0202 - Happy Number

Difficulty: Easy

Pattern:
- Set
- Cycle Detection
- Digit Processing

Topics (LeetCode):
- Hash Table
- Math
- Two Pointers

Time Complexity: O(log n)

Auxiliary Space Complexity: O(log n)

Complexity Explanation:
The complexity depends on the number of digits in n, not on the numeric
value of n itself.

A number n has O(log n) digits. The inner loop processes each digit once,
so processing the initial number takes O(log n) time.

For a number with d digits, each digit contributes at most 9^2 = 81.
Therefore, after one transformation, the next value is at most 81 * d.
Since d = O(log n), the generated values quickly shrink to a range bounded
relative to the number of digits rather than growing up to n.

The set stores previously generated values for cycle detection. It does not
store every value from 1 to n. Because the generated states are bounded by
the digit-square transformation, the auxiliary space is O(log n).

Set membership and insertion are O(1) on average.

Date Solved: 2026-08-02
Last Reinforced: N/A

Notes:
Repeatedly calculates the sum of the squares of the digits and stores
each generated value in a set. Reaching 1 means the number is happy,
while encountering a previously seen value detects a cycle and means
the number is not happy.
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        total = 0
        seen = set()

        while total != 1:
            total = 0

            while n != 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

            if total not in seen:
                seen.add(total)
            else:
                return False

        return True