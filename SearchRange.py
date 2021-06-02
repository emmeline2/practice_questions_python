class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target is None or nums is None:
            return [-1, -1]
        
        retList = [-1, -1]
    
        for index in range(len(nums)):
            if nums[index] == target and retList[0] == -1:
                retList[0] = index
                retList[1] = index
            elif nums[index] == target: 
                retList[1] = index
            elif nums[index] > target:
                # The array is sorted, so break out of for loop if above target
                break 
                
        
        
        return retList
