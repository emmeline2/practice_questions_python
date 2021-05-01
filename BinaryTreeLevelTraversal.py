# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def levelOrder(self, root):
        level=1
        current=(root, level)
        s=set()
        result=[]
        if root is None:
            return result
        Q = [current]
        while Q:
            current=Q.pop()
            level=current[1]
            if current[0] is not None:
                if current[0] not in s:
                    result.append([current[0].val, level])
                    s.add(current[0])
                if current[0].left:
                    Q.insert(0,(current[0].left, level+1))
                if current[0].right:
                    Q.insert(0,(current[0].right, level+1))
        output=[]
        temp=[]
        level=1
        for val in result:
            if val[1]==level:
                temp.append(val[0])
            elif val[1] > level:
                output.append(temp)
                temp=[val[0]]
                level+=1
        output.append(temp)
        return output
