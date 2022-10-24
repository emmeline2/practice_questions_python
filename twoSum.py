class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indicies = {}
        
        for index in range(0, len(nums)):
            indicies[index] = nums[index]
            
        
        
        for index in range(0, len(nums)): 
            temp = target - nums[index]
            
            if temp in indicies.values():
                key = indicies.keys()[indicies.values().index(temp)]
                if key != index:
                    return [index, key]
        
        print("not found")
        return [-1, -1]
        
