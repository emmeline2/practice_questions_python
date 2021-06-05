class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0: 
            return 0
        
        dp = [0] * len(nums)
        
        dp[0] = 1
        maxans = 1
        
        for i in range(1, len(dp)):
            maxval = 0
            
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])

            dp[i] = maxval + 1
            maxans = max(maxans, dp[i])
        
        return maxans
