class Solution:
    def openLock(self, deadends, target: str) -> int:
        q = []
        
        if "0000" in deadends:
            return -1

        q.append(["0000", 0])
        
        visited = set()
        visited.add("0000")        
        while len(q) > 0:
            front, step = q[0]
            del q[0]

            
            if front == target:
                return step
            
            for i, c in enumerate(front):
            
                p1 = front[:i] + str((int(c) - 1) % 10) + front[i + 1:]
                p2 = front[:i] + str((int(c) + 1) % 10) + front[i + 1:]
                if p1 not in deadends and p1 not in visited:
                    visited.add(p1)
                    q.append([p1, step + 1])
                if p2 not in deadends and p2 not in visited:
                    visited.add(p2)
                    q.append([p2, step + 1])
                
        return -1


print(Solution().openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))