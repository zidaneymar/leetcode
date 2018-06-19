# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        tuples = []
        while cur and cur.next:
            tuples.append((cur, cur.next))
            cur = cur.next.next
        if cur:
            tuples.append((cur, None))
        for i in range(0, len(tuples)):
            if tuples[i][1]:
                tuples[i][1].next = tuples[i][0]
            if i + 1 < len(tuples):
                if tuples[i+1][1]:
                    tuples[i][0].next = tuples[i+1][1]
                else:
                    tuples[i][0].next = tuples[i+1][0]
            elif i + 1 == len(tuples):
                tuples[i][0].next = None
        return tuples[0][1]


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
# c.next = d


x = Solution()
res = x.swapPairs(a)
