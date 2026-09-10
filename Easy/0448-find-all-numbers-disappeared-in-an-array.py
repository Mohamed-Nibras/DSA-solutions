"""
LeetCode 0448 - Find All Numbers Disappeared in an Array

Difficulty: Easy

Pattern:
- Set Membership
- Range Traversal

Topics (LeetCode):
- Array
- Hash Table

Time Complexity: O(n)

Auxiliary Space Complexity: O(n)

Complexity Explanation:
The input array is converted into a set, which takes O(n) time.

The algorithm then traverses every number from 1 to n. Each membership
check in the set takes O(1) average time.

Therefore, the overall time complexity is O(n).

The set can store up to n unique elements, resulting in O(n)
auxiliary space.

Date Solved: 2026-09-10

Notes:
Checks every expected number in the range from 1 to n and returns
all numbers that are not present in the input array.
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in n:
                result.append(i)

        return result