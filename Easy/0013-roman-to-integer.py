"""
LeetCode 0013 - Roman to Integer

Difficulty: Easy

Pattern:
- Hash Map
- String Traversal

Topics (LeetCode):
- Hash Table
- Math
- String

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
Date Solved: 2026-09-20
Last Reinforced: N/A

Notes:
Compare each Roman numeral with the next one. If the current value is smaller,
subtract it; otherwise, add it. The final numeral is added separately.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        integer = 0

        for i in range(len(s) - 1):

            if roman[s[i]] < roman[s[i + 1]]:
                integer -= roman[s[i]]
            else:
                integer += roman[s[i]]

        return integer + roman[s[-1]]