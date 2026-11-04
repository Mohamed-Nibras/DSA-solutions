"""
LeetCode 1207 - Unique Number of Occurrences

Difficulty: Easy

Pattern:
- Frequency Counting
- Hash Set

Topics (LeetCode):
- Array
- Hash Table

Time Complexity: O(n)
Auxiliary Space Complexity: O(n)

Date Solved: 2026-11-04
Last Reinforced: N/A

Notes:
- Used Counter to calculate the frequency of each distinct number.
- Used a set to track frequencies already encountered.
- If a frequency already exists in the set, return False.
- If all frequencies are unique, return True.
"""


from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        frequency = Counter(arr)
        unique = set()

        for i, j in frequency.items():
            if j not in unique:
                unique.add(j)
            else:
                return False

        return True