import sys  # Import sys module for sys.maxsize

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_value = sys.maxsize  # Initialize min_value with maximum possible value

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val <= self.min_value:
            self.min_stack.append(val)
            self.min_value = val

    def pop(self):
        """
        :rtype: None
        """
        if not self.is_empty():
            popped_item = self.stack.pop()
            if popped_item == self.min_value:
                self.min_stack.pop()
                if self.min_stack:
                    self.min_value = self.min_stack[-1]
                else:
                    self.min_value = sys.maxsize
                return popped_item
            else:
                return popped_item
        else:
            raise IndexError("pop from an empty stack")

    def top(self):
        """
        :rtype: int
        """
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def getMin(self):
        """
        :rtype: int
        """
        if not self.is_empty():
            return self.min_value
        else:
            raise IndexError("getMin from an empty stack")

