# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pointer1 = head
        pointer2 = head
        pre = None 
        for i in range(0, n):
            pointer2 = pointer2.next
        while pointer2 != None:
            pre = pointer1
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        if pre:
            pre.next = pointer1.next
        else:
            return head.next
        return head



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()
res = s.removeNthFromEnd(a, 2)