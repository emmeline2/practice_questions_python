class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        minimum = nums[0]
        
        # if no rotation
        if nums[right] > nums[0]: 
            return nums[0]
        
        # search
        while left <= right: 
            pivot = left + (right - left) // 2 
            
            if nums[pivot] > nums[pivot + 1]:
                return nums[pivot + 1]
            if nums[pivot - 1] > nums[pivot]:
                return nums[pivot]
            
            if nums[pivot] < nums[left]: 
                right = pivot - 1
            else:
                left = pivot + 1
                
            

        
