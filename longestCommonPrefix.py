# Trie node definition
class tNode(object):
    def __init__(self):
        self.val=None
        self.child=None

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # empty edge case
        if not strs:
            return ''
    
        # Save root reference
        root=tNode()
        node=root
        # iterate characeters in first string and add to trie
        for character in strs[0]:
            node.val=character
            node.child=tNode()
            node=node.child
        
        # iterate over other words
        for word in strs[1:]:
            node=root
            for character in word:
                if node.val==character:
                    node=node.child
                else:
                    break
            node.val=None
            node.child=None
        
        prefix=''
        node=root
        while node.val:
            prefix+=node.val
            node=node.child
        return prefix
