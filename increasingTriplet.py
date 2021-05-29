class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
                
        if len(nums) < 3:
            return False
        
        # iterate for previous index to len
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if (nums[i] < nums[j] < nums[k]):
                        return True

        return False
                
        
