class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ones_found = 0
        max_ones = 0
        
        for i in range(0, len(nums)): 
            if nums[i] == 1:
                ones_found += 1
            else: 
                if ones_found > max_ones: 
                    max_ones = ones_found
                ones_found = 0
        
        # account for if last number is a 1
        return max(ones_found, max_ones)
