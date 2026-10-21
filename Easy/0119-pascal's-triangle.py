"""
LeetCode 118 - Pascal's Triangle

Difficulty: Easy

Pattern:
- Previous Row Construction
- Adjacent Pair Summation

Topics (LeetCode):
- Array
- Dynamic Programming

Time Complexity: O(n^2)
Auxiliary Space Complexity: O(n^2) including the output triangle

Date Solved: 2026-10-21
Last Reinforced: N/A

Notes:
- Initialize the triangle with the first row [1].
- Construct each subsequent row using the previous row.
- Every new row begins and ends with 1.
- Calculate the middle elements by adding adjacent elements from
  the previous row.
- Append each completed row to the triangle.
- Return the triangle containing the requested number of rows.
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]

        for i in range(1, numRows):
            previous = triangle[-1]
            new = [1]

            for k in range(len(previous) - 1):
                value = previous[k] + previous[k + 1]
                new.append(value)

            new.append(1)
            triangle.append(new)

        return triangle