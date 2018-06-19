#Definition for singly-linked list.
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
            
        c1 = l1
        c2 = l2
        p1 = None
        while c2 != None:
            if not c1:
                c1 = ListNode(0)
                p1.next = c1
            p1 = c1
            c1.val += c2.val
            c1 = c1.next
            c2 = c2.next

        c1 = l1
        remain = None
        p1 = None
        while c1 != None:
            if c1.val >= 10:
                remain = int(c1.val / 10)
                c1.val = c1.val % 10
            p1 = c1
            c1 = c1.next
            if remain:
                if not c1:
                    c1 = ListNode(remain)
                    p1.next = c1
                else:
                    c1.val += remain
                remain = None
        return l1

        
        
    def getReversedList(self, l1: ListNode) -> ListNode:
        cur = l1
        stack = list()
        while cur != None:
            stack.append(cur)
            cur = cur.next 
        
        cur = None
        pre = None
        head = None
        while len(stack):
            cur = ListNode(stack.pop().val)
            if pre != None and cur != None:
                pre.next = cur
            if not pre:
                head = cur    
            pre = cur
        return head
        
    def convertListNodeToNumber(self, l1 : ListNode) -> int:
        res = 0
        cur = l1
        base = 1
        while cur != None:
            res += cur.val * base
            base *= 10
            cur = cur.next
        return res

    def convertNumberToListNode(self, num: int) -> ListNode:
        if num == 0:
            return ListNode(0)
        head = None
        pre = None
        cur = None
        while num != 0:
            p = num % 10
            cur = ListNode(p)
            if not head:
                head = cur
            if pre:
                pre.next = cur
            pre = cur
            num = (int)(num / 10)
        return head


s = Solution()

a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)
d.next = e
e.next = f

x = s.addTwoNumbers(a, d)
print(x)