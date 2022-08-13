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
        
        # create return list for running sums
        ret_list = []
        ret_list.append(nums[0])

        # create running sums list
        # increment from 1 -> end, skipping 0 index
        for i in range(1,len(nums)):
            sum = ret_list[i-1] + nums[i]
            ret_list.append(sum)
        
        return ret_list
