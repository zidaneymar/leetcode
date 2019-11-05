class Solution:
    
    
    def dfs(self, graph, node, mem, visited):

        if node in mem:
            return mem[node]
        
        if node in visited:
            return True
        
        visited.add(node)
        for i in graph[node]:
            res = self.dfs(graph, i, mem, visited)
            if res:
                
                mem[node] = True
                return True
            
        mem[node] = False
        return False
        
    def eventualSafeNodes(self, graph):
        
        res = []
        for i in range(len(graph)):
            if not self.dfs(graph, i, {}, set()):
                res.append(i)
        return res

print(Solution().eventualSafeNodes([[1],[0]]))