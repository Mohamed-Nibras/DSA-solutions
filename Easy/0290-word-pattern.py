"""
LeetCode 0290 - Word Pattern

Difficulty: Easy

Pattern:
- Hash Map
- Bidirectional Mapping

Topics (LeetCode):
- Hash Table
- String

Time Complexity: O(n)

Auxiliary Space Complexity: O(n)

Date Solved: 2026-07-24
Last Reinforced: N/A

Notes:
Maintains two hash maps to enforce a one-to-one relationship between
pattern characters and words. One map stores character → word while
the other stores word → character. Every new mapping is validated
before insertion to ensure consistency in both directions.
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        character_to_word = {}
        word_to_character = {}

        for character, word in zip(pattern, words):

            if character in character_to_word:
                if character_to_word[character] != word:
                    return False

            else:
                if word in word_to_character:
                    return False

                character_to_word[character] = word
                word_to_character[word] = character

        return True