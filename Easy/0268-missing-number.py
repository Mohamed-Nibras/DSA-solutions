"""
LeetCode 0268 - Missing Number

Difficulty: Easy

Pattern:
- Set Membership
- Range Traversal

Topics (LeetCode):
- Array
- Hash Table
- Math
- Binary Search
- Bit Manipulation
- Sorting

Time Complexity: O(n)

Auxiliary Space Complexity: O(n)

Complexity Explanation:
The input list is first converted into a set, which takes O(n) time.

The algorithm then checks every number from 0 to n. Set membership
checking takes O(1) average time.

Therefore, the overall time complexity is O(n).

The set stores up to n elements, resulting in O(n) auxiliary space.

Date Solved: 2026-09-09

Notes:
The solution checks every expected number from 0 to n and returns
the number that is not present in the input set.

Alternative Approaches Studied:
- Mathematical Sum: O(n) time, O(1) auxiliary space.
- XOR: O(n) time, O(1) auxiliary space.
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        value = len(nums)

        for i in range(0, value + 1):
            if i not in s:
                return i