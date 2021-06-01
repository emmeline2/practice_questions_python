class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums is None or k is None: 
            return []
        
        elements = {}
        
        
        for num in nums:
            if num not in elements:
                elements[num] = 1
            else:
                elements[num] = elements[num] + 1
        
        # create a heap of top k frequencey elemens and convert it into an output array
        return heapq.nlargest(k, elements.keys(), key=elements.get)
