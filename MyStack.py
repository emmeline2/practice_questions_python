class MyStack(object):

    def __init__(self):
        self.my_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.my_stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.my_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        max_index = len(self.my_stack) - 1
        return self.my_stack[max_index]
        
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.my_stack) is None or len(self.my_stack) is 0: 
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
