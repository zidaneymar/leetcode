# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head == None:
            return None
        helping_list = []
        
        cur = head
        while cur != None:
            helping_list.append(cur)
            cur = cur.next
        
        list_len = len(helping_list) # 3

        rotate_len = k % list_len # 1 

        new_bound = list_len - rotate_len# 2

        before = helping_list[new_bound:]
        after = helping_list[0: new_bound]
        new_list = before + after
        for i in range(0, len(new_list) - 1):
            new_list[i].next = new_list[i + 1]
        new_list[len(new_list) - 1].next = None

        return new_list[0]

x = Solution()

a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
a.next = b
b.next = c

print (x.rotateRight(a, 4))
            