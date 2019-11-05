import collections

class Solution:
    
    def dfs(self, charIndex, curString, stickers, mem):
        if len(curString) == 0:
            return 0

        if curString in mem:
            return mem[curString]
               
        curTarget = collections.Counter(curString)
        total = float('inf')
        for c in curTarget:
            # for a single character c, we have different choices to deduct the cost
            for choice in charIndex[c]:
                
                index = choice[0]

                tempTarget = curTarget.copy()

                count = collections.Counter(stickers[index])
                for ch in count:
                    if ch in curTarget:
                        curTarget[ch] = max(0, curTarget[ch] - count[ch])

                nextString = ""
                for unit in curTarget:
                    nextString += curTarget[unit] * unit

                nextString = "".join(sorted(nextString))
                
                cur = self.dfs(charIndex, nextString, stickers, mem) + 1

                curTarget = tempTarget

                total = min(cur, total)
        mem[curString] = total
        return total
    
    def minStickers(self, stickers, target: str) -> int:

        buff = ""

        for s in stickers:
            buff += s
        
        target = "".join(sorted(target))
        
        buffCount = collections.Counter(buff)

        for t in target:
            if t not in buffCount:
                return -1
                

        charIndex = {}
        
        for i, stick in enumerate(stickers):
            cn = collections.Counter(stick)
            
            for c in cn:
                if c not in charIndex:
                    charIndex[c] = [(i, cn[c])]
                else:
                    charIndex[c] += [(i, cn[c])]
                    
        
        return self.dfs(charIndex, target, stickers, {})
print(Solution().minStickers(
["soil","since","lift","are","lot","twenty","put"],
"appearreason"))