class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        mid = len(nums) // 2
        
        numbers = {}
        
        for element in nums:
            if element in numbers:
                numbers[element] += 1
            else:
                numbers[element] = 1
            
            if numbers[element] > mid: 
                return element
        
        # majority emenet not found
        return -1
