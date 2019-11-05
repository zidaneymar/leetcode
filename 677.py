class TrieNode:
    def __init__(self):
        self.score = 0
        self.val = 0
        self.isWord = False
        self.children = [None] * 26
    
    def insert(self, key, val):
        
        if len(key) == 0:
            diff = 0
            if self.isWord:
                diff += val - self.val
            else:
                diff += val
                self.isWord = True
            self.score += diff
            self.val = val
            return diff
            
        
        index = ord(key[0]) - ord('a')
        if self.children[index] == None:
            self.children[index] = TrieNode()
        
        subDiff = self.children[index].insert(key[1:], val)
        self.score += subDiff
        
        return subDiff
        
    def find(self, key):
        
        if len(key) == 0:
            return self.score
        index = ord(key[0]) - ord('a')
        
        if self.children[index] == None:
            return 0
        
        return self.children[index].find(key[1:])
        
        
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        self.root.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.root.find(prefix)


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert('aa',3)
obj.insert('aa', 2)
obj.insert('aaa', 3)
obj.insert('abcdd', 111)
param_2 = obj.sum('a')
print(param_2)