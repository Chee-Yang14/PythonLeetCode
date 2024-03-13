class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []  # Initialize ans as an empty list
        
        # Calculate left products
        # for nums = [1,2,3,4]
        # ans would look like this ans = [1,1,2,6]
        left_product = 1
        for i in range(n):
            ans.append(left_product)
            left_product *= nums[i]
        
        # Calculate right products and multiply with existing ans
        # for nums = [1,2,3,4]
        # ans would look like this ans = [24,12,4,1]
        right_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
        
        #mutiplying both together you get the answer: ans =[24,12,8,6]
        
        return ans