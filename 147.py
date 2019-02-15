# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        
        while cur:
            if not prev:
                prev = cur
                cur = cur.next
                continue
            if prev.val > cur.val: #invalid, should invert the cur to the first one smaller than it
                cur2 = head
                prev2 = None  
                while cur2 and cur2.val < cur.val:
                    prev2 = cur2
                    cur2 = cur2.next
                if not prev2:
                    # the insertion index is the head of linkedlist
                    head = cur
                    temp = cur.next
                    cur.next = cur2
                    cur = temp
                    prev.next = cur
                else:
                    prev2.next = cur
                    temp = cur.next
                    cur.next = cur2
                    prev.next = temp
                    cur = temp
            else:
                prev = cur
                cur = cur.next
                
        return head

a = ListNode(-1)
b = ListNode(5)
c = ListNode(3)
d = ListNode(4)
e = ListNode(0)
a.next = b
b.next = c
c.next = d
d.next = e
x = Solution()
print(x.insertionSortList(a))