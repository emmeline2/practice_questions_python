class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        
        # initialize array
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            # calculate sum of house two back and current house, or use previous house
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        # return last index
        return dp[len(nums)-1]
