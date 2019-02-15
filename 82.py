# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fakeHead = ListNode(0)
        fakeHead.next = head

        prev = fakeHead
        cur = head

        while cur != None:
            while cur.next != None and cur.val == cur.next.val:
                cur = cur.next
            if prev.next == cur:
                prev = cur
            else:
                prev.next = cur.next
            cur = cur.next
        
        return fakeHead.next
    