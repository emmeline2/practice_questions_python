class Solution(object):
    def isPalindrome(self, substring):
        """
        :type s: str
        :rtype: bool
        """
        end = len(substring) - 1
        retval = True

        for start in range(len(substring)/2):
            if substring[start] != substring[end]:
                retval = False
                break
    
        return retval
            
        
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        max_len = 0
        max_palindrome = ""
        
        if s is None:
            return max_palindrome
        if len(s) == 1:
            return s
        
        for l_index in range(0,len(s) - 1):
            for r_index in range(l_index+1, len(s)):
                if self.isPalindrome(s[l_index:r_index]): 
                    length = r_index - l_index
                    if length > max_len:
                        max_len = length
                        max_palindrome = s[l_index:r_index]

        
        return max_palindrome
        
