class Solution(object):
    def majorityElement(self, nums):

        majority = len(nums)/2
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for key in freq.keys():
            if freq[key] > majority:
                return key
            
a = Solution()
print(a.majorityElement([2,2,1,1,1,2,2]))
            