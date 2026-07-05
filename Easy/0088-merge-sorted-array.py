class Solution(object):
    def merge(self, nums1, m, nums2, n):

        
        i = m - 1
        j = n - 1
        k = len(nums1) - 1
        while(j != -1):
            if i == -1:
                nums1[k] = (nums2[j])
                j -= 1
                k -= 1
                continue
            
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            
            elif nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        
    
a = Solution()
nums1 = [4,5,6,0,0,0]
a.merge(nums1,3,[1,2,3],3)
print(nums1)