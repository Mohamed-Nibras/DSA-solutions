"""
LeetCode 0219 - Contains Duplicate II

Difficulty: Easy

Pattern:
- Hash Map
- Last Seen Index Tracking

Topics (LeetCode):
- Array
- Hash Table
- Sliding Window

Time Complexity: O(n)

Auxiliary Space Complexity: O(n)

Date Solved: 2026-07-22
Last Reinforced: N/A

Notes:
Stores the most recent index of each element using a hash map.
When a duplicate is encountered, compares the current index with the
last stored index. If the distance is at most k, a valid nearby duplicate
exists. Otherwise, updates the stored index to the current occurrence.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_seen = {}

        for i, value in enumerate(nums):
            if value in last_seen:
                if i - last_seen[value] <= k:
                    return True

            last_seen[value] = i

        return False