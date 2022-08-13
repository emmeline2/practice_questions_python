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
        """
        
        # input checks ---------------------------
        if nums is None: 
            return None
        if len(nums) is 1:
            return 0

            
        # calculate right running sum ---------------------
        # create a copy of nums
        right_sum = nums[:]
        
        # range from end(excluding last) -> 0 (range is non inclusive), decrementing
        for i in range(len(nums)-2, 0-1, -1): 
            temp_sum = right_sum[i+1] + nums[i]
            right_sum[i] = temp_sum
        

        # calculte left running sum  ------------------------
        left_sum = []
        left_sum.append(nums[0])
        # check if zero index is the pivot
        if left_sum[0] == right_sum[0]:
                return 0
        for i in range(1, len(nums)): 
            temp_sum = left_sum[i-1] + nums[i]
            left_sum.append(temp_sum)
    
            # check if pivot value by comparing against right
            if left_sum[i] == right_sum[i]:
                return i
        
        # no index is found
        return -1
            
