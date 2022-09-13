# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: 
            return []
        
        largest_vals = []
        level = [(root, root.val)]
        
        while level: 
            new_level = []
            
            # add max value to largest list
            # finds max of the values for each node (element 1 in list)
            max_for_level = max(map(lambda x: x[1], level))
            largest_vals.append(max_for_level)
            
            # add next nodes to the list
            for node, value in level: 
                if node.left: 
                    new_level.append((node.left, node.left.val))
                if node.right:
                    new_level.append((node.right, node.right.val))
            
            level = new_level
                
        
        
        return largest_vals
