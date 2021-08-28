# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0 
        if root is None: 
            return count
        
        count = self.traverse(root)
        return count
        
    
    def traverse(self, root): 
        if root == None: 
            return 0
        
        if root.left == None or root.right == None:
            return self.traverse(root.left) + self.traverse(root.right) + 1
        
        return min(self.traverse(root.right), self.traverse(root.left)) + 1
