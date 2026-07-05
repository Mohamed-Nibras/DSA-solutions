class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        freq = {}
        if len(s) != len(t):
            return False
        
        for letter in s:
            freq[letter]= freq.get(letter, 0) + 1

        for i in t:
            if i in freq:
                freq[i] -= 1
            else:
                return False

        return all(value == 0 for value in freq.values())
        
   

a = Solution()
print(a.isAnagram("car", "rat"))