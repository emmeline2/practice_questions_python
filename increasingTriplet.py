class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        num_1,num_2 = 2**31-1,2**31-1
        
        for num_3 in nums:
            if num_3 < num_1:
                # reset num_1 to new smallest
                num_1 = num_3

            elif num_1 < num_3 < num_2:
                # reset num_2 to next smallest
                num_2 = num_3

            elif num_3 > num_2:
                # in this case num1 < num2 < num3, return true
                return True
        
        # if iterate whole list and don't find anything return false
        return False
