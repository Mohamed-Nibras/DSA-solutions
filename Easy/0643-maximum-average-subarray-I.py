"""
LeetCode 0643 - Maximum Average Subarray I

Difficulty: Easy

Pattern:
- Sliding Window

Topics (LeetCode):
- Array
- Sliding Window

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)
Date Solved: 2026-10-02
Last Reinforced: N/A

Notes:
Maintain the sum of the current subarray of length k using a sliding
window. Start with the first k elements, then remove the element leaving
the window and add the element entering it. Track the maximum average
throughout the traversal.

Core Pattern:
INITIAL WINDOW → REMOVE OUTGOING → ADD INCOMING → UPDATE MAXIMUM

The incoming element for window starting at index i is nums[k + i - 1],
while the outgoing element is nums[i - 1].

Using the running window sum avoids recalculating the sum for every
subarray, reducing the time complexity from O(n * k) to O(n).

Learning:
Initially approached the problem by calculating the sum of every possible
window separately, which resulted in O(n * k) complexity and TLE.
Recognized and implemented the Sliding Window pattern by maintaining and
updating the running window sum in O(1) time for each shift.
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
    
        total = sum(nums[:k])
        maximum_average = total/float(k)

        for i in range(1, len(nums) - k + 1):

            total = (total - nums[i - 1] + nums[k + i -1])
            
            average = total/float(k)

            if maximum_average < average:
                maximum_average = average

        return maximum_average