"""
LeetCode 0345 - Reverse Vowels of a String

Difficulty: Easy

Pattern:
- Two Pointers
- In-Place Swapping

Topics (LeetCode):
- Two Pointers
- String

Time Complexity: O(n)

Auxiliary Space Complexity: O(n)

Date Solved: 2026-09-15
Last Reinforced: N/A

Notes:
Uses two pointers from opposite ends, skips consonants, and swaps vowels
until the pointers meet. The string is converted to a list for modification
and joined back into a string at the end.
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "AEIOUaeiou"

        i = 0
        j = len(s) - 1

        l = list(s)

        while (i < j):

            if l[i] in vowels and l[j] in vowels:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1

            elif l[j] not in vowels:
                j -= 1

            elif l[i] not in vowels:
                i += 1

        return "".join(l)