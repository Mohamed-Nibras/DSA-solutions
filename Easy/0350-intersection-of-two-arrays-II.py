"""
LeetCode 350 - Intersection of Two Arrays II

Difficulty: Easy

Pattern:
- Frequency Counting
- Hash Map

Topics (LeetCode):
- Array
- Hash Table
- Two Pointers
- Binary Search
- Sorting

Time Complexity: O(n + m)

Auxiliary Space Complexity: O(n)

Date Solved: 2026-09-17
Last Reinforced: N/A

Notes:
The initial approach traversed the frequency map and checked whether each
distinct value existed in nums2, which could process each value only once and
therefore could not correctly preserve duplicate occurrences. Traversing
nums2 instead allows each occurrence to consume one available frequency from
nums1, producing the correct intersection with duplicates.
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        freq = {}

        for i in nums1:
            freq[i] = freq.get(i, 0) + 1

        result = []

        for i in nums2:
            if i in freq:
                if freq[i] != 0:
                    result.append(i)
                    freq[i] -= 1

        return result