# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        # create root node at midpoint
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        
        # create left and right sides of binary search tree
        
        # left is everything up to mid point
        node.left = self.sortedArrayToBST(nums[:mid])
        
        # right is everything past the mid point
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
