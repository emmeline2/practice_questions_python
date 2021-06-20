class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_stack = []
        
        for paren in s:
            if paren == "(" or paren == "{" or paren == "[":
                left_stack.append(paren)
            else:
                if len(left_stack) == 0:
                    # nothing in the stack to pop
                    return False
                left = left_stack.pop()
                if (paren == ")") and not (left == "("):
                    return False
                elif (paren == "}") and not (left == "{"):
                    return False
                elif (paren == "]") and not (left == "["):
                    return False
        
        if len(left_stack) > 0:
            # something left in the stack
            return False
        return True
        
