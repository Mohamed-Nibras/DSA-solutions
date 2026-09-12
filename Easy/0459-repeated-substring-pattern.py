"""
LeetCode 0459 - Repeated Substring Pattern

Difficulty: Easy

Pattern:
- Brute Force
- Prefix Testing

Topics (LeetCode):
- String
- String Matching
- Z Algorithm
- Knuth–Morris–Pratt Algorithm

Time Complexity: O(n²)

Auxiliary Space Complexity: O(n)

Date Solved: 2026-09-12
Last Reinforced: N/A

Notes:
Tries every possible prefix length up to half of the string. Each prefix
is repeated enough times to check whether it reconstructs the original
string. A valid repeating substring must occur at least twice.
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        k = 1

        for i in range(1, len(s) // 2 + 1):
            candidate = s[:k]
            copies = len(s) // k

            if candidate * copies == s:
                return True

            k += 1

        return False