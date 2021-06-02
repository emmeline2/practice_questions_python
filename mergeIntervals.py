class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals is None or len(intervals)==0: 
            return []
        
        
        current_min = intervals[0][0]
        current_max = intervals[0][1]
        
        retList = []
        
        
        for interval in intervals:
            min = interval[0]
            max = interval[1]
            
            if min <= current_max and max >= current_max: 
                current_max = interval[1]
            
            if min > current_max:
                retList.append([current_min, current_max])
                current_min = min
                current_max = max
        
        if retList[len(retList)-1][1] != max:
            retList.append([current_min, current_max])
        
        
        return retList
            
                
        
