class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result_l = []
        result_r = []
        left_product = 1
        right_product = 1
        for i in range(len(nums)):
            # product = 1
            # for j in range(len(nums)):
            #     if j == i:
            #         continue
                
            #     product *= nums[j]
            # result.append(product

            result_l.append(left_product)
            left_product *= nums[i]

        for i in range(len(nums) -1, -1, -1):
               result_r.append(right_product)
               right_product *= nums[i]
        
        return [i * j for i, j in zip(result_l, reversed(result_r))]


A = Solution()
print(A.productExceptSelf([1,2, 3, 4]))