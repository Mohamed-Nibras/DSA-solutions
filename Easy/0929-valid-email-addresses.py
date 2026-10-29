class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

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


A = Solution()
print(A.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))