"""
LeetCode 0058 - Length of Last Word

Difficulty: Easy

Pattern:
- String Processing
- String Manipulation

Topics (LeetCode):
- String

Time Complexity: O(n)

Auxiliary Space Complexity: O(n)

Complexity Explanation:
The split() operation processes the input string and creates a list
containing the words, requiring O(n) time and O(n) auxiliary space
in the worst case.

Accessing the last word and retrieving its length take O(1) time.

Date Solved: 2026-09-06

Notes:
The string is split into words using split(), which automatically
handles leading, trailing, and multiple spaces. The length of the
last word is then returned.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()

        return len(words[-1])