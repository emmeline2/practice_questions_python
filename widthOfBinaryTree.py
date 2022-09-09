# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        width = 0
        # start with root level
        level = [(root, 0)]

        while level:
            new_level = []
            width = max(width, level[-1][1] - level[0][1] + 1)
            
            for node, pos in level:
                if node.left:
                    new_level.append((node.left, pos * 2))
                if node.right:
                    new_level.append((node.right, pos * 2 + 1))
            
            level = new_level
        
        return width
