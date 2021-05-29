class Solution:
    def lengthOfLongestSubstring(self, s):
        map = {}
        left = right = 0
        count = 0
        max_count = 0
        
        if s is None: 
            return count
        if len(s) is 1: 
            return count + 1
        
        
        while right < len(s):
            r = s[right]
            if r in map:
                max_count = max(max_count, count)
                right = left
                left += 1
                map.clear()
                count = 0
            else:
                map[r] = 1
                count += 1
                right += 1
        
        # set max value, in case if is never reached
        max_count = max(max_count, count)
        return max_count
