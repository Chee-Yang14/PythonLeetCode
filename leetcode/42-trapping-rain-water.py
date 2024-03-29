class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        maxLeft =0
        maxRight= 0
        left = 0
        right = len(height)-1
        
        while left < right:
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])
            
            if height[left] < maxLeft:
                maxWater += maxLeft-height[left]
            if height[right] < maxRight:
                maxWater += maxRight - height[right]

            if height[left] <= height[right]:
                left +=1
            if height[right] < height[left]:
                right -= 1

        
        return maxWater