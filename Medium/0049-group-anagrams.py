"""
LeetCode 49 - Group Anagrams

Difficulty: Medium

Pattern:
- Character Frequency Counting
- Hash Map Grouping
- Frequency Signature

Topics (LeetCode):
- Array
- Hash Table
- String
- Sorting

Time Complexity: O(n * k log k)
Auxiliary Space Complexity: O(n * k)

Date Solved: 2026-10-05
Last Reinforced: N/A

Notes:
- Count the frequency of each character for every word.
- Convert the character-frequency pairs into a sorted tuple to create a consistent,
  hashable signature for each anagram group.
- Use the signature as a dictionary key and store all words with the same signature
  in the corresponding list.
- Return the grouped lists using list(freq.values()).
- This was my first Medium problem. The implementation required significant
  guidance, but the complete data-structure flow and implementation were
  understood before reconstructing the accepted solution.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq = {}

        for word in strs:

            count = {} # DICTIONARY THAT STORES FREQUENCY FOR EACH WORD, AND REFRESHES FOR EVERY WORD

            for letter in word:

                count[letter] = count.get(letter, 0) + 1

            signature = tuple(sorted(count.items())) # CHANGES THE COUNT DICT TO A TUPLE THAT HAS THE FREQUENCY INFORMATION

            if signature not in freq:
                freq[signature] = []

            freq[signature].append(word)

        return list(freq.values())
    
A = Solution()
print(A.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))