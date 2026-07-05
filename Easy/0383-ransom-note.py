class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        mag = {}
        ransom = {}

        for i in magazine:
            mag[i] = mag.get(i, 0) + 1

        for i in ransomNote:
            ransom[i] = ransom.get(i, 0) + 1


        for key in ransom:
            if key not in mag or mag[key] < ransom[key]:
                return False
            else:
                if mag[key] >= ransom[key]:
                        result = True
        return result

a = Solution()
print(a.canConstruct("aa", "aab"))
        
        