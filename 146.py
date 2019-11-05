class Node:
    def __init(self):
        self.prev = None
        self.next = None
        self.val = None
        self.key = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cur = 0
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        res = self.dict[key]
        # remove the linked list
        res.prev.next = res.next
        res.next.prev = res.prev
        
        # insert at head
        res.next = self.head.next
        res.prev = self.head
        self.head.next = res
        res.next.prev = res

        return res.val
        
        
    def put(self, key: int, value: int) -> None:

        if key in self.dict:
            temp = self.dict[key]
            self.get(key)
            temp.val = value
            return


        if self.cur < self.cap:
            newNode = Node()
            newNode.val = value
            newNode.next = self.head.next
            newNode.prev = self.head
            newNode.key = key
            newNode.next.prev = newNode

            self.head.next = newNode
            self.dict[key] = newNode
            self.cur += 1
        else:
            
            temp = self.tail.prev
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

            del self.dict[temp.key]
            newNode = Node()
            newNode.val = value
            newNode.key = value
            newNode.next = self.head.next
            newNode.prev = self.head
            newNode.next.prev = newNode
            self.head.next = newNode
            self.dict[key] = newNode
        
# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)

print(obj.get(2))
obj.put(3,2)
print(obj.get(2))
print(obj.get(3))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)