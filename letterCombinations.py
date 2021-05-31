class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
            return []
        
        map = {}
        map[2] = {'a','b', 'c'}
        map[3] = {'d', 'e', 'f'}
        map[4] = {'g', 'h', 'i'}
        map[5] = {'j', 'k', 'l'}
        map[6] = {'m', 'n', 'o'}
        map[7] = {'p', 'q', 'r', 's'}
        map[8] = {'t', 'u', 'v'}
        map[9] = {'w', 'x', 'y', 'z'}
        
        results = ['']
        
        for digit in digits:
            results = [result+d for result in results for d in map[int(digit)]]
            
        
        return results
