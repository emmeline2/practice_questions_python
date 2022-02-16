class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        curr = -1
        
        for number in nums:
            if number != (curr + 1): 
                return curr + 1
            else: 
                curr = curr + 1
        
        # reached end
        return (curr + 1)
