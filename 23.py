# Definition for singly-linked list.
from queue import PriorityQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # class OrderedListNode:
    #     def __init__(self, val):
    #         self.val = val
    #         self.next = None
    #     def __lt__(self, other):
    #         return self.val < other.val
    def mergeKLists(self, lists: list):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        q = PriorityQueue()
        for l in lists:
            cur = l
            while cur:
                q.put(cur.val)
                cur = cur.next
        head = None
        pre = None
        while not q.empty():
            cur = q.get()
            if not head:
                head = ListNode(cur)
                pre = head
            else:
                curNode = ListNode(cur)
                if pre:
                    pre.next = curNode
                pre = curNode
                
        return head

x = Solution()
a = ListNode(1)
b = ListNode(2)
a.next = b

c = ListNode(3)

d = x.mergeKLists([a, c])