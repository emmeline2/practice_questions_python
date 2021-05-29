class Solution(object):
    
    def getLengthSubstring(self, substring):
        if len(substring) is 0: 
            return 0
        if len(substring) is 1:
            return 1
        
        map = {}
        cmax = 0
        count = 0
        
        for c in substring:
            if c not in map:
                count += 1
                map[c] = 1
            else:
                cmax = max(cmax, count)
                count = 0
                map.clear()
        
        return cmax
    
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0;
        for index in range(len(s)):
            max_count = max(max_count, self.getLengthSubstring(s[index:]))
        
        return max_count
            
    

            
            
