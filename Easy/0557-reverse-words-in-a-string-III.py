"""
LeetCode 0557 - Reverse Words in a String III

Difficulty: Easy

Pattern:
- String Manipulation
- String Reversal

Topics (LeetCode):
- Two Pointers
- String

Time Complexity: O(n)

Auxiliary Space Complexity: O(n)

Date Solved: 2026-09-14
Last Reinforced: N/A

Notes:
Splits the sentence into words, reverses each word using slicing, and joins
them back together while preserving the original word order. An alternative
can update the same words list using words[i] = words[i][::-1], avoiding a
separate result list, though the overall auxiliary space complexity remains O(n).
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()
        word = []

        for i in words:
            i = i[::-1]
            word.append(i)

        return " ".join(word)