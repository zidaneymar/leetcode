class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        if len(self._min) > 0 and x <= self._min[-1]:
            self._min.append(x)
        elif len(self._min) == 0:
            self._min.append(x)
            
    def pop(self):
        """
        :rtype: void
        """
        top = self._stack[-1]
        self._stack.pop()
        if len(self._min) > 0 and top == self._min[-1]:
            self._min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)