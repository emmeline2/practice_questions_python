# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        response = []
        if root is None:
            return response
        
        self.traverse(root, response)
        return response
    
    def traverse(self, root, list):
        if root is None:
            pass
        else:
            # add left
            if root.left is not None:
                self.traverse(root.left, list)
            
            # add right
            if root.right is not None:
                self.traverse(root.right, list)
            
            # add node
            list.append(root.val)
        
