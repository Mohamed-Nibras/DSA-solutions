class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sub = [i for i in s]
        main = [i for i in t]

        if not s:
            return True 
        index = 0
        for i in range(len(sub)):
            result = False
            for j in range(index, len(main)):
                if sub[i] == main[j]:
                    result = True
                    index = j + 1
                    break
            if not result:
                return False 
            
        return result

a = Solution()
print(a.isSubsequence("axc", "ahbxdc"))