class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # input has no elements
        if strs is None:
            return [[""]]
        
        # input has one element
        if len(strs) is 1:
            return [strs]
        
        
        answer = collections.defaultdict(list)
        for s in strs:
            # for each item in strs, sort the string and add
            # the item to its matching key (sorted string)
            answer[tuple(sorted(s))].append(s)
 
        # return just the value sets
        return answer.values()
