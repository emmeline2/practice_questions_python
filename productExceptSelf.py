class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
      
        total_product = 1
        zero_count = 0
        
        # calcuate total product and zero count
        for i in range(len(nums)):
            if nums[i] != 0:
                total_product *= nums[i]
            else:
                zero_count += 1
        
        result = []
        
        # if more than one zero - whole list is zero
        if zero_count > 1:
            result = [0] * len(nums)
            return result
            
        # calcuate product if no other elements are zeros
        for i in range(len(nums)):
            if nums[i] != 0:
                if zero_count:
                    result.append(0)
                else:
                    result.append(total_product / nums[i])
            else:
                # if is a zero return product of all other non zero elements
                result.append(total_product)
        
        
        return result
