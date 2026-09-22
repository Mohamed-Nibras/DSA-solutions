"""
LeetCode 0844 - Backspace String Compare

Difficulty: Easy

Pattern:
- Stack / LIFO

Topics (LeetCode):
- Two Pointers
- String
- Stack
- Simulation

Time Complexity: O(n + m)
Auxiliary Space Complexity: O(n + m)

Date Solved: 2026-09-22
Last Reinforced: N/A

Notes:
Use a stack to simulate typing. Push normal characters and pop the most recent
character when '#' is encountered, if the stack is not empty. Compare the
resulting strings.
"""


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_stack = []
        t_stack = []

        for i in s:
            if i != "#":
                s_stack.append(i)

            else:
                if s_stack:
                    s_stack.pop(-1)

        for i in t:
            if i != "#":
                t_stack.append(i)

            else:
                if t_stack:
                    t_stack.pop(-1)

        return "".join(s_stack) == "".join(t_stack)