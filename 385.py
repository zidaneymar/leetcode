# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def getNumber(self, s):
        for i in range(0, len(s)):
            if not s[i].isdigit() and s[i] != '-':
                return int(s[:i])
        return None
    def findNextPair(self, s):
        stack = []
        if s[0] != '[':
            return -1
        stack.append(s[0])
        for i in range(1, len(s)):
            if s[i] == ']':
                stack.pop()
            elif s[i] == '[':
                stack.append('[')
            if len(stack) == 0:
                return i + 1
        return -1

    def deserializeList(self, s: str):
        
    def deserialize(self, s: str) -> NestedInteger:
        res = None
        if len(s) == 0 or not s:
            return NestedInteger()
        if s[0] == '[':
            # is list
            ni = self.findNextPair(s)
            res.add(self.deserialize[s[0:ni]])
            res = NestedInteger()
            index = s.find(',')
            if index > 0:
                res.add(self.deserialize(s[:index]))
                res.add(self.deserialize(s[index+1:]))
            else:
                res.add(self.deserialize(s))
        else:
            num = self.getNumber(s)
            res = NestedInteger()
            if num:
                res.setInteger(num)
            
        return res


print(Solution().deserialize("[2,[],5,[3,4]]"))