"""
LeetCode 599 - Minimum Index Sum of Two Lists

Difficulty: Easy

Pattern:
- Hash Map
- Index Tracking

Topics (LeetCode):
- Array
- Hash Table
- String

Time Complexity: O(n + m)

Auxiliary Space Complexity: O(n)

Date Solved: 2026-09-18
Last Reinforced: N/A

Notes:
The key is to track the minimum sum of the indices of common restaurants.
When a smaller sum is found, replace the current result; when an equal
minimum is found, add the restaurant to the result.
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        pair = []

        minimum = float('inf')

        for i in range(len(list1)):
            if list1[i] in list2:
                index_sum = i + list2.index(list1[i])

                if index_sum < minimum:
                    minimum = index_sum
                    pair = []
                    pair.append(list1[i])

                elif index_sum == minimum:
                    pair.append(list1[i])

        return pair