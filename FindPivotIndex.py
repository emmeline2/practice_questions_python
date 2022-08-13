class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Example: 
        [1,7,3,6,5,6]
        running sum from the left
        [1,8,11,17,22,28]
        running sum from right
        [28,27,20,17,11,6]
        Pivot = index 3 (17)
        
        Given:
        S is total sum of numbers
        - At index i, the sum of all left numbers + number at i + right sum = total sum 
        - So, total sum - number at i - sum of left numbers = right sum 
        - So, only need total sum and current running left sum to check if it is the pivot
        """
        
        # input checks ---------------------------
        if nums is None: 
            return None
        if len(nums) is 1:
            return 0

        # calculate pivot -------------------------
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(0, len(nums)):
            if left_sum == (total_sum - left_sum - nums[i]):
                return i
            left_sum = left_sum + nums[i]

        
        # no index is found ------------------------
        return -1
            
