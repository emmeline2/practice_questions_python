# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        response = []
        self.traverse(root, response)
        return response
    
    def traverse(self, root, list):
        if root is None:
            pass
        else:
            if root.left is not None:
                self.traverse(root.left, list)
            list.append(root.val)
            if root.right is not None: 
                self.traverse(root.right, list)
