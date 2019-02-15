class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n <= m:
            return head
        fakeHead = ListNode(0)
        fakeHead.next = head

        cur = head
        pre = fakeHead
        i = 1

        tag1 = None
        tag2 = None
        while cur != None:
            if i == m:
                tag1 = pre
                tag2 = cur
                pre = cur
                cur = cur.next
            elif i > m and i < n:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            elif i == n:
                tag1.next = cur
                tag2.next = cur.next
                cur.next = pre
                pre = cur 
                cur = cur.next
                break
            elif i < m:
                pre = cur
                cur = cur.next
            i += 1
        return fakeHead.next
x = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e


print(x.reverseBetween(a, 1, 2))