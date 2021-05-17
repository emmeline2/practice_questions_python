class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # error cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # define relative max to be the largest number in array
        rel_max = max(nums)

        current_sum = 0
        
        # iterate the list and calcuate a running sum
        for i in range(len(nums)):
            if current_sum+nums[i] < 0:
                # if current sum becomes less than zero, reset current_sum to zero
                # any sum after this element will be greater if you restart from zero
                current_sum = 0
            else:
                # add the current item to current sum
                current_sum = current_sum + nums[i]
                # re assign the relative max if the current sum is greater
                rel_max = max(rel_max, current_sum)
        return rel_max
