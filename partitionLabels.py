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
                

        end = 0
        start = 0
        ans = []
        
        
        # loop the string, increasing the partition based on last seen
        # value for each character encountered
        for i in range(0, len(s)):
            end = max(end, last_seen[s[i]])
            # break the partition when incrementing i reaches the max end value
            if i == end:
                # get length, +1 to convert from indexes
                ans.append(i - start + 1)
                start = i + 1
        
        return ans
