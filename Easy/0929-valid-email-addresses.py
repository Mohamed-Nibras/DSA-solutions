"""
LeetCode 929 - Unique Email Addresses

Difficulty: Easy

Pattern:
- String Normalization
- Hash Set

Topics (LeetCode):
- Array
- String
- Hash Table

Time Complexity: O(n * m)
Auxiliary Space Complexity: O(n * m)

Date Solved: 2026-10-29
Last Reinforced: N/A

Notes:
- Split each email into its local name and domain using "@".
- If "+" exists in the local name, ignore it and everything
  after the first "+".
- Remove all periods from the remaining local name.
- Combine the normalized local name with the original domain.
- Store normalized email addresses in a set to eliminate
  duplicates.
- Return the number of unique email addresses.
"""


class Solution(object):
    def numUniqueEmails(self, emails):

        unique = set()

        for email in emails:
            domain = email.split("@")
            local = domain[0]

            for i in range(len(local)):
                if local[i] == "+":
                    local = local[:i]
                    break

            local = local.replace(".", "")
            domain[0] = local
            unique.add(domain[0] + "@" + domain[1])

        return len(unique)