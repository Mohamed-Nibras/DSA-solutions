"""
LeetCode 1047 - Remove All Adjacent Duplicates In String

Difficulty: Easy

Pattern:
- Stack
- Adjacent Duplicate Removal

Topics (LeetCode):
- String
- Stack

Time Complexity: O(n)
Auxiliary Space Complexity: O(n)

Date Solved: 2026-10-06
Last Reinforced: N/A

Notes:
- Use a list as a stack to maintain the characters that remain after removing
  adjacent duplicates.
- For each character, compare it with the top of the stack.
- If the characters match, remove the top character; otherwise, add the current
  character to the stack.
- The remaining characters are joined to form the final string.
"""


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        duplicate = []

        for i in s:
            if duplicate:
                if duplicate[-1] == i:
                    duplicate.pop()

                else:
                    duplicate.append(i)

            else:
                duplicate.append(i)

        return "".join(duplicate)