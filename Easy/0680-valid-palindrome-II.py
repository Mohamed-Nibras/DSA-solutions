"""
LeetCode 0680 - Valid Palindrome II

Difficulty: Easy

Pattern:
- Two Pointers
- Palindrome Checking
- Greedy Choice

Topics (LeetCode):
- Two Pointers
- String
- Greedy

Time Complexity: O(n)

Auxiliary Space Complexity: O(1)

Complexity Explanation:
The main two-pointer traversal checks characters from both ends and
stops at the first mismatch.

At the first mismatch, at most two remaining ranges are checked:
one by skipping the left character and one by skipping the right
character. Each range is traversed at most once, so the overall
time complexity remains O(n).

The algorithm uses only pointer variables and does not create
additional strings or data structures, giving O(1) auxiliary space.

Date Solved: 2026-09-02
Last Reinforced: N/A

Notes:
At the first mismatch, check both possibilities: skip the left
character or skip the right character, and verify whether either
remaining range is a palindrome.
"""


class Solution(object):
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(left, right):
                while left < right:
                    if s[left] != s[right]:
                        return False
                    left += 1
                    right -= 1
                return True
        
        left = 0
        right = len(s) - 1

        while (left < right):
            if s[left] != s[right]:
                    return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
                

            left += 1
            right -= 1

        return True