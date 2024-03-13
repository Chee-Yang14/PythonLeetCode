class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []  # Initialize ans as an empty list
        
        # Calculate left products
        left_product = 1
        for i in range(n):
            ans.append(left_product)
            left_product *= nums[i]
        
        # Calculate right products and multiply with existing ans
        right_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
        
        return ans