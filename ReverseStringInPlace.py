class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            # swap left and right
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            # increment left
            left += 1
            # decrement right
            right -= 1
    
