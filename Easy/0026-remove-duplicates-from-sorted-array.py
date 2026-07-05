class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        
        for i in nums:
            if i not in result:
                result.append(i)
        for i in range(len(result)):
            nums[i] = result[i]
                
        return len(result)

a = Solution()
print(a.removeDuplicates([1, 1, 2]))        