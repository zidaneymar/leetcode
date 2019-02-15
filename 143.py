# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        
        cur = head
        index = 0
        mem = {}
        
        while cur:
            mem[index] = cur
            cur = cur.next
            index += 1
        
        prev = None
        
        for i in range(0, int((index + 1) / 2)):
            if prev:
                prev.next = mem[i]                
            mem[i].next = mem[index - i - 1]
            if index % 2 == 1 and i == index - i - 1:
                mem[i].next = None
            if index % 2 == 0 and i == index 
            prev = mem[index - 1- i]
        
        

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b 
b.next = c
c.next = d

x = Solution()
print(x.reorderList(a))