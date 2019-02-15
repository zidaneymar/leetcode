import collections
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        mem = collections.OrderedDict()
        
        tickets.sort(key=lambda x: x[0])
        
        for ticket in tickets:
            if ticket[0] not in mem:
                mem[ticket[0]] = [(ticket[1], False)]
            else:
                mem[ticket[0]].append((ticket[1], False))
        
        for key in mem:
            mem[key].sort()

        
        def dfs(cur, depth):
            if depth == 1:
                return [cur]
            
            for desti, used in mem[cur]:
                if not used:
                    
                    res = [cur] + dfs(desti, depth - 1)
                    if len(res) == depth:
                        return res
            return []
        
        return dfs("JFK", len(tickets) + 1)
        
            
        
        
            
print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))