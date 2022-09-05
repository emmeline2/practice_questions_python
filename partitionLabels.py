class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
                
        #last = {c: i for i, c in enumerate(s)}
        
        
        # create hash map of last seen occurance of each letter
        last_seen = {}
        for i in range(0, len(s)): 
            if s[i] in last_seen: 
                last_seen[s[i]] = i
            else: 
                last_seen[s[i]] = i
                

        curr_max = 0
        anchor = 0
        ans = []
        for i, c in enumerate(s):
            curr_max = max(curr_max, last_seen[c])
            if i == curr_max:
                ans.append(i - anchor + 1)
                anchor = i + 1
        
        return ans
