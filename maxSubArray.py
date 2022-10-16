class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        currMax = nums[0]
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            currMax = max(currMax+nums[i], nums[i])
            maxSum = max(maxSum, currMax)
        
        return maxSum
