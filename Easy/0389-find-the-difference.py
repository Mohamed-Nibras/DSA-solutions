"""
LeetCode 0389 - Find the Difference

Difficulty: Easy

Pattern:
- Frequency Map
- Character Frequency Counting

Topics (LeetCode):
- Hash Table
- String
- Bit Manipulation
- Sorting

Time Complexity: O(n)

Auxiliary Space Complexity: O(k)

Complexity Explanation:
Counter(t) builds a frequency map for the characters in t.
The characters of s are then traversed once to subtract their
frequencies from the corresponding entries.

Finally, the frequency map is traversed to find the character whose
remaining frequency is 1, which represents the extra character added
to t.

The strings are traversed a constant number of times, giving an
overall time complexity of O(n).

The frequency map stores one entry for each distinct character,
where k is the number of distinct characters. Therefore, the
auxiliary space complexity is O(k).

If the character set is fixed and bounded, k can be treated as a
constant, making the auxiliary space effectively O(1).

Date Solved: 2026-09-04
Last Reinforced: N/A

Notes:
Uses character frequencies from t and subtracts the frequencies
present in s. The remaining character with frequency 1 is the
extra character.
"""

from collections import Counter


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq = Counter(t)

        for i in s:
            freq[i] -= 1

        for i in freq:
            if freq[i] == 1:
                return i