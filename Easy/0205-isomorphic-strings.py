class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
    
        s_list = [i for i in s]
        t_list = [i for i in t]

        dictionary = {}
        i = 0

        for i in range(len(s)):
            if s[i] not in dictionary and t[i] not in dictionary.values():
                dictionary[s[i]] = t[i]
            
            elif t[i] in dictionary.values() and s[i] not in dictionary:
                return False
            
            elif dictionary[s[i]] != t[i]:
                return False 
            
        return True

a = Solution()
print(a.isIsomorphic("paper", "title"))