"""
LeetCode 0409 - Longest Palindrome

Difficulty: Easy

Pattern:
- Frequency Counting
- Palindrome Construction

Topics:
- Hash Table
- String
- Greedy

Approach:
Count the frequency of every character.

Characters with even frequencies can be fully used because they can
be placed equally on both sides of the palindrome.

For characters with odd frequencies, their largest even portion can
always be used. Only one odd-frequency character can contribute its
remaining character as the center of the palindrome.

Time Complexity: O(n)
Auxiliary Space Complexity: O(n)

Date Solved: 2026-09-11
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}

        for i in s:
            freq[i] = freq.get(i, 0) + 1

        result = 0
        center = True

        for i, j in freq.items():
            if j % 2 == 0:
                result += j

            elif j % 2 != 0:
                if center:
                    result += j
                    center = False
                else:
                    result += j - 1

        return result