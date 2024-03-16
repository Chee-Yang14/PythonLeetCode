class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #make sure nums is not empty
        if not nums:
            return 0

        #make it a set to remove duplicate
        num_set = set(nums)
        #use to keep track of the highest streak
        longest_streak = 0

        #first iterate through the set and see if each individual numbers continue a sequence
        #while loop is used to find the longest streak using the number from the first for loops
        # once the while loop is done and the streak is found, the for loop continue on to the next number
        #the if statement is used so it only count on numbers that start in the begining
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak