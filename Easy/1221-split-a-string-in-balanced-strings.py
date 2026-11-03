"""
LeetCode 1221 - Split a String in Balanced Strings

Difficulty: Easy

Pattern:
- Frequency Counting
- State Tracking
- Greedy

Topics (LeetCode):
- String
- Greedy
- Counting

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)

Date Solved: 2026-11-03
Last Reinforced: N/A

Notes:
- Maintain separate counters for the occurrences of 'R' and 'L'.
- Traverse the string and increment the corresponding counter
  for each character.
- Whenever both counters become equal, a balanced substring
  has been completed.
- Increment the balanced substring count and reset both
  counters to zero.
- Continue until the entire string has been traversed.
- Return the total number of balanced substrings.
"""


class Solution(object):
    def balancedStringSplit(self, s):

        R = 0
        L = 0
        count = 0

        for i in range(len(s)):
            if s[i] == "R":
                R += 1

            elif s[i] == "L":
                L += 1

            if s[i] == "R" and (R == L):
                count += 1
                R = 0
                L = 0

            if s[i] == "L" and (R == L):
                count += 1
                R = 0
                L = 0

        return count