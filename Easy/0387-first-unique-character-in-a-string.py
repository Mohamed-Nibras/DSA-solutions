"""
LeetCode 0387 - First Unique Character in a String

Difficulty: Easy

Pattern:
- Frequency Map
- String Traversal
- First Unique Element Detection

Topics (LeetCode):
- Hash Table
- String
- Queue

Time Complexity: O(n)

Auxiliary Space Complexity: O(k)

Complexity Explanation:
The first pass traverses the string once to build a frequency map,
storing the number of occurrences of each character.

The second pass traverses the original string from left to right.
For each character, its frequency is checked in the dictionary.
The first character whose frequency is exactly 1 is the first unique
character, so its original index is returned.

Both passes take O(n) time, giving an overall time complexity of O(n).

The frequency dictionary stores one entry for each distinct character,
where k is the number of distinct characters in the string. Therefore,
the auxiliary space complexity is O(k).

If the character set is fixed and bounded, k can be treated as a
constant, making the auxiliary space effectively O(1).

Date Solved: 2026-09-01
Last Reinforced: N/A

Notes:
A frequency map alone cannot determine which unique character appears
first. Therefore, two passes are used: the first pass determines the
frequency of every character, while the second pass preserves the
original ordering of the string and returns the index of the first
character whose frequency is 1.
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        freq = {}

        for i in s:
            freq[i] = freq.get(i, 0) + 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1