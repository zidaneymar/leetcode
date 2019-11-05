class UF:
    def __init__(self):
        self.parent = {}
        self.value = {}
        self.added = set()
    def find(self, v):
        if v not in self.parent:
            self.parent[v] = v
            self.value[v] = 1
        elif self.parent[v] != v:
            prev = self.parent[v]
            self.parent[v] = self.find(self.parent[v])
            self.value[v] *= self.value[prev]
            
        return self.parent[v]
    
    def union(self, v1, v2, value):
        p1, p2 = self.find(v1), self.find(v2)
        
        self.parent[p1] = p2
        self.value[v1] = value * self.value[v2]
    
    def search(self, v1, v2):
        if v1 not in self.added or v2 not in self.added:
            return -1.0
        if v1 == v2:
            return 1.0
        if self.find(v1) != self.find(v2):
            return -1.0
        else:
            return self.value[v1] * (1 / self.value[v2])

    def add(self, v):
        self.added.add(v)


class Solution:
    def calcEquation(self, equations, values, queries):
        
        temp = UF()
        
        for i, e in enumerate(equations):
            temp.add(e[0])
            temp.add(e[1])
            p1, p2 = map(temp.find, e)
            if p1 != p2:
                temp.union(e[0], e[1], values[i])
        
        res = []

        for v1, v2 in queries:
            res.append(temp.search(v1, v2))
        return res
        

print(Solution().calcEquation([["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],
[3.0,0.5,3.4,5.6],
[["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]))