class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = set()
        for i in nums:
            if i in result:
                return True
            else:
                result.add(i)
        return False

a = Solution()
print(a.containsDuplicate([1, 2, 3, 4, 4]))
        