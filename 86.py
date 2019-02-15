# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lowerHead = ListNode(0)
        lowerHead.next = None

        largerHead = ListNode(0)
        largerHead.next = None

        lowerCur = lowerHead
        largerCur = largerHead

        cur = head

        while cur != None:
            if cur.val < x:
                lowerCur.next = cur
                lowerCur = cur 
            else:
                largerCur.next = cur
                largerCur = cur
            cur = cur.next
        
        lowerCur.next = largerHead.next
        largerCur.next = None
        return lowerHead.next


a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

x = Solution()
head = x.partition(a, 3)

print(head)