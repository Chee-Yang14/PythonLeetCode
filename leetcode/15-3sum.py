class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element of the triplet
            
            left, right = i + 1, len(nums) - 1  # Initialize two pointers
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Move the left pointer to increase the sum
                elif total > 0:
                    right -= 1  # Move the right pointer to decrease the sum
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates for the second element of the triplet
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates for the third element of the triplet
                    left += 1
                    right -= 1
                
        return ans