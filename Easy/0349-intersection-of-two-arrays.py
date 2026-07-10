"""
LeetCode 0349 - Intersection of Two Arrays

Difficulty: Easy

Pattern:
- Set
- Set Membership Checking

Topics (LeetCode):
- Array
- Hash Table
- Two Pointers
- Binary Search
- Sorting

Time Complexity: O(n + m)
Auxiliary Space Complexity: O(n + m)

Date Solved: 2026-07-10
Last Reinforced: N/A

Notes:
Reinforced the use of sets for duplicate removal and efficient membership checking.
Also learned Python's set intersection operator (&) as an alternative syntax.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        unique = []
        seen1 = set(nums1)
        seen2 = set(nums2)
        for i in seen1:
            if i in seen2:
                unique.append(i)

        return unique

        # Alternative in just a single line is
        # return list(set(nums1) & set(nums2))

a = Solution()
print(a.intersection([1, 2, 3, 4, 5], [1, 2, 4]))