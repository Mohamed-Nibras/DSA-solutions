"""
LeetCode 0028 - Find the Index of the First Occurrence in a String

Difficulty: Easy

Pattern:
- String Traversal
- Brute Force Substring Search
- Two Pointers

Topics (LeetCode):
- Two Pointers
- String
- String Matching

Time Complexity: O(n * m)

Auxiliary Space Complexity: O(1)

Complexity Explanation:
The algorithm may attempt to match the needle starting from multiple
positions in the haystack.

For each starting position, characters may be compared until a
mismatch occurs or the entire needle is matched.

In the worst case, up to n starting positions may be checked, with
up to m character comparisons for each attempt.

Therefore, the worst-case time complexity is O(n * m), where n is
the length of haystack and m is the length of needle.

Only a constant number of variables are used, so the auxiliary space
complexity is O(1).

Date Solved: 2026-09-07

Notes:
Uses two indices to compare consecutive characters and a start
variable to track the beginning of the current matching attempt.
When a mismatch occurs, matching restarts from the next possible
starting position.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        j = 0
        start = 0

        if needle == "":
            return 0

        while j < len(needle) and i < len(haystack):

            if haystack[i] == needle[j]:
                i += 1
                j += 1
                result = start

            elif haystack[i] != needle[j]:
                start += 1
                j = 0
                i = start

        if j == len(needle):
            return result
        else:
            return -1