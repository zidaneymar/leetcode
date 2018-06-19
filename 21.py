# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        cur = None
        pre = None
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                if not head:
                    head = ListNode(p1.val)
                    pre = head
                else:
                    cur = ListNode(p1.val)
                    pre.next = cur
                    pre = cur
                p1 = p1.next
            else:
                if not head:
                    head = ListNode(p2.val)
                    pre = head
                else:
                    cur = ListNode(p2.val)
                    pre.next = cur
                    pre = cur
                p2 = p2.next
        if p1:
            if pre:
                pre.next = p1
            else:
                head = p1
        if p2:
            if pre:
                pre.next = p2
            else:
                head = p2

        
        return head



