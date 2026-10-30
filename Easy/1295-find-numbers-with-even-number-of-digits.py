"""
LeetCode 1295 - Find Numbers with Even Number of Digits

Difficulty: Easy

Pattern:
- Digit Counting
- Mathematical Operations

Topics (LeetCode):
- Array
- Math

Time Complexity: O(n * d)
Auxiliary Space Complexity: O(1)

Date Solved: 2026-10-30
Last Reinforced: N/A

Notes:
- Traverse each number in the input array.
- Use a temporary variable to preserve the original number.
- Count the digits by repeatedly performing integer division
  by 10 until the temporary number becomes zero.
- Check whether the digit count is even using the modulo operator.
- Increment the result whenever a number has an even digit count.
- Return the total count of numbers with an even number of digits.
"""


class Solution(object):
    def findNumbers(self, nums):

        even = 0

        for num in nums:
            n = num
            count = 0

            while n != 0:
                count += 1
                n //= 10

            if count % 2 == 0:
                even += 1

        return even