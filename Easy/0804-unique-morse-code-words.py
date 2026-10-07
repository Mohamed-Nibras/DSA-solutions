"""
LeetCode 804 - Unique Morse Code Words

Difficulty: Easy

Pattern:
- String Encoding
- Hash Map

Topics (LeetCode):
- Array
- Hash Table
- String

Time Complexity: O(S)
Auxiliary Space Complexity: O(S)

Date Solved: 2026-10-07
Last Reinforced: N/A

Notes:
- Use a Morse-code mapping to convert each character into its corresponding
  Morse representation.
- Build the complete Morse representation for each word by concatenating
  the encoded characters.
- Store each completed transformation and count its occurrences using a
  hash map.
- The number of unique keys in the hash map represents the number of
  different Morse-code transformations.
"""


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = {"a":".-",
                 "b":"-...",
                 "c":"-.-.",
                 "d":"-..",
                 "e":".",
                 "f":"..-.",
                 "g":"--.",
                 "h":"....",
                 "i":"..",
                 "j":".---",
                 "k":"-.-",
                 "l":".-..",
                 "m":"--",
                 "n":"-.",
                 "o":"---",
                 "p":".--.",
                 "q":"--.-",
                 "r":".-.",
                 "s":"...",
                 "t":"-",
                 "u":"..-",
                 "v":"...-",
                 "w":".--",
                 "x":"-..-",
                 "y":"-.--",
                 "z":"--.."}

        seen = []

        for word in words:
            current = ""

            for letter in word:
                current += morse[letter]

            seen.append(current)

        result = {}
        for word in seen:
            result[word] = result.get(word, 0) + 1

        return len(result)