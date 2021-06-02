class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals is None or len(intervals)==0: 
            return []

        intervals.sort()

        retList = []
        
        for interval in intervals:
            if not retList or retList[-1][1] < interval[0]: 
                retList.append(interval)
            
            else:
                retList[-1][1] = max(retList[-1][1], interval[1])
        

        return retList
            
                
        
