class Solution:
    def longestPalindrome(self, s):
        result_str = ""
        
        for i in range(len(s)):
            # this is for odd length palindrome
            word1 = self.checkPalindrome(s, i, i)
            # this is for even length palindrome
            word2 = self.checkPalindrome(s, i, i+1)
            
            # word1 will be max length word from word1 and word2
            word1 = word1 if len(word1) >= len(word2) else word2 
            
            # compare word1 with our result
            result_str = word1 if len(word1) >= len(result_str) else result_str
            
        return result_str
    
    def checkPalindrome(self, s, low, high):
        # expand as long as 'lo' can grow to the left
        # and 'hi' and grow to the right and chracters at those indexes match
        while (low >= 0) and (high < len(s)) and (s[low]==s[high]):
            low -= 1
            high += 1
        
        # return the slice from original string that starts from our last matched index of low and high.
        # We don't increament high because python slice goes up to ending index-1
        return s[low+1:high]
