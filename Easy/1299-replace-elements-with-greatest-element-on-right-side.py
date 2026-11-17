"""
LeetCode 1299 - Replace Elements with Greatest Element on Right Side

Difficulty: Easy

Pattern:
- Array Traversal
- Running Maximum
- Right-to-Left Traversal

Topics (LeetCode):
- Array

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)

Date Solved: 2026-11-17
Last Reinforced: N/A

Notes:
Initial attempts used slicing and repeated max() calculations to find
the greatest element to the right of each position. Although logically
correct, these approaches resulted in O(n²) time complexity.

The optimized approach traverses the array from right to left while
maintaining a running maximum.

For each position:
1. Preserve the original element in a temporary variable.
2. Replace the current element with the greatest value found so far.
3. Update the running maximum using the preserved original value.

Initialize the running maximum to -1 so the last element is also
replaced correctly.

This approach modifies the original array in-place and achieves
O(n) time complexity with O(1) auxiliary space.

Learning Status:
Optimized implementation understood. Successfully understood
right-to-left traversal, running maximum maintenance, and the
importance of preserving the original element before replacement.

Optimization Learned:
Instead of repeatedly calculating the maximum of the remaining
elements, maintain the greatest value while traversing backwards.
"""


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        greatest = -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]

            arr[i] = greatest

            greatest = max(greatest, current)

        return arr