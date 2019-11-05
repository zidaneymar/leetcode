class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    def find(self, v):
        if v not in self.parent:
            self.parent[v] = v
            self.rank[v] = 0
        elif self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, v1, v2):
        p1, p2 = map(self.find, [v1, v2])
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
            
        
class Solution:
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        dset = DisjointSet()
        
        for e in edges:
            ps, pe = map(dset.find, e)
            if ps == pe:
                return e
            dset.union(e[0], e[1])
        