"""
LeetCode 496 - Next Greater Element I

Difficulty: Easy

Pattern:
- Linear Search
- Forward Traversal

Topics (LeetCode):
- Array
- Hash Table
- Stack
- Monotonic Stack

Time Complexity: O(n * m)
Auxiliary Space Complexity: O(n)

Date Solved: 2026-10-08
Last Reinforced: N/A

Notes:
- For each element in nums1, first locate its corresponding position in nums2.
- Starting from that position, scan to the right until the first greater
  element is found.
- If no greater element exists, append -1.
- This solution prioritizes direct problem decomposition and correctness.
- The solution was accepted on the first implementation attempt.
"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        result = []

        k = None

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                maximum = -1
                if nums1[i] == nums2[j]:
                    k = j
                    while k < len(nums2):
                        if nums2[k] > nums1[i]:
                            maximum = nums2[k]
                            break
                        k += 1
                        
                    result.append(maximum)

        return result