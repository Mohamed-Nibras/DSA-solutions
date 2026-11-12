"""
LeetCode 1160 - Find Words That Can Be Formed by Characters

Difficulty: Easy

Pattern:
- Character Frequency Counting
- Hash Map / Counter

Topics (LeetCode):
- Array
- Hash Table
- String
- Counting

Time Complexity: O(C + W)
Auxiliary Space Complexity: O(C + W)
Date Solved: 2026-11-12
Last Reinforced: N/A

Notes:
Use Counter to calculate the available character frequencies from chars
and the required character frequencies for each word.

Check whether every character required by a word is available in sufficient
quantity. If all character requirements are satisfied, add the word's
length to the total.

Each word is checked independently against the original character
frequencies. Characters are not consumed between different words.
"""


from collections import Counter


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        total = 0
        freq_char = Counter(chars)

        for word in words:
            freq = Counter(word)
            is_there = True

            for key in freq:
                if key not in freq_char:
                    is_there = False
                    break

                elif key in freq_char and freq[key] <= freq_char[key]:
                    is_there = True
                    continue

                else:
                    is_there = False
                    break

            if is_there:
                total += len(word)

        return total