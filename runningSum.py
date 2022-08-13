class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # corner cases
        if len(nums) is None: 
            return None
        elif len(nums) is 1: 
            return nums

        # Write over input array to save space
        # increment from 1 -> end, skipping 0 index
        for i in range(1,len(nums)):
            sum = nums[i-1] + nums[i]
            nums[i] = sum
        
        return nums
