class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]: return 0
            else: return 1
            
        # index variables for left and right of peak
        i = 0
        k = 2
        
        # iterate the list in groups of 3
        for j in range(1,len(nums)-1):
            if nums[i] < nums[j] and nums[j] > nums[k]:
                return j
            # increment two side indexes
            i = i + 1
            k = k + 1
        
        # Edge cases
        if nums[k-1] > nums[j]:
            return k-1
        if nums[0] > nums[1]:
            return 0
        
        # no peaks found
        return 0
            
