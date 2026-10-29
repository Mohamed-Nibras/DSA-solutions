
"""
LeetCode 941 - Valid Mountain Array

Difficulty: Easy

Pattern:
- Increasing and Decreasing Sequence
- State Tracking

Topics (LeetCode):
- Array

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)

Date Solved: 2026-10-26
Last Reinforced: N/A

Notes:
- Return False if the array contains fewer than three elements.
- Track whether an increasing sequence has occurred and whether
  the sequence has started decreasing.
- Elements must strictly increase before the peak and strictly
  decrease after the peak.
- Equal adjacent elements and any increase after the descent
  begins make the array invalid.
- Return True only when both the increasing and decreasing
  phases have occurred.
"""


class Solution(object):
    def validMountainArray(self, arr):

        if len(arr) < 3:
            return False

        increase = False
        decrease = False

        for i in range(1, len(arr)):

            if arr[i] > arr[i - 1] and not decrease:
                increase = True

            elif increase and arr[i] < arr[i - 1]:
                decrease = True
                
            else:
                return False

        return increase and decrease