"""
LeetCode 1002 - Find Common Characters

Difficulty: Easy

Pattern:
- Character Frequency Counting
- Minimum Frequency Tracking
- Hash Map / Counter

Topics (LeetCode):
- Array
- Hash Table
- String

Time Complexity: O(n * m)
Auxiliary Space Complexity: O(k)

Where:
- n = number of words
- m = maximum length of a word
- k = number of distinct characters (at most 26)

Date Solved: 2026-10-27
Last Reinforced: N/A

Notes:
- Initialize a Counter using the first word.
- Count the characters in each subsequent word.
- Update each tracked character's frequency to the minimum
  of its current frequency and its frequency in the new word.
- Set a character's frequency to zero if it is absent from
  the current word.
- Build the result list by repeating each character according
  to its remaining common frequency.
"""


from collections import Counter

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = Counter(words[0])
        result = []

        for word in words:
            current = Counter(word)

            for key in common:
                if key in current:
                    common[key] = min(current[key], common[key])

                else:
                    common[key] = 0

        for i in common:
            for _ in range(common[i]):
                result.append(i)

        return result