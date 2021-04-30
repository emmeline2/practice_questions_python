# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BinaryTreeLevelTraversal(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.list = []
        self.index = int(0)
        if root is None:
            return self.list
        self.list.insert(self.index, [root.val])
        self.index = self.index + 1
        self.levelList = []
        self.getLevel(root)
        return self.list
    
    def getLevel(self, root):
        empty = True
        if root is None:
            return
        
        if root.left is not None:
            empty = False
            self.levelList.append(root.left.val)
        if root.right is not None:
            empty = False
            self.levelList.append(root.right.val)
        
        if not empty:
            print "List adding: ", self.levelList
            self.list.insert(self.index, self.levelList)
            self.levelList = []
            self.index = self.index + 1
            self.getLevel(root.left)
            self.getLevel(root.right)
            return
        else:
            return
