"""
LeetCode 0003 - Longest Substring Without Repeating Characters

Difficulty: Medium

Pattern:
- Sliding Window
- Hash Map / Last Seen Index Tracking

Topics (LeetCode):
- Hash Table
- String
- Sliding Window

Time Complexity: O(n)
Auxiliary Space Complexity: O(min(n, character set size))
Date Solved: 2026-11-13
Last Reinforced: N/A

Notes:
Initial attempt used string manipulation to maintain a substring without
repeating characters. However, handling duplicates and maintaining the
correct substring boundaries proved difficult.

The optimized approach uses a sliding window with two pointers (left and
right) and a dictionary to track the last seen index of each character.

When a repeated character appears inside the current window, move the
left boundary to one position after its previous occurrence. Calculate
the current window length and maintain the maximum length.

Learning Status:
Guided solution studied. The sliding window concept and dictionary
index-tracking syntax are not yet fully understood.

Reinforcement Required:
Independently re-solve the problem and explain the sliding window
boundary updates without referring to the solution.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        already_seen = {}
        left = 0
        max_length = 0

        for right in range(len(s)):

            if s[right] in already_seen and already_seen[s[right]] >= left:
                left = already_seen[s[right]] + 1

            already_seen[s[right]] = right

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length