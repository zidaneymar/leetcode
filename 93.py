class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def dfs(curNums: list, index: int, count: int, curNum: str):
            if count == 4 and index >= len(s):
                res.append(".".join(curNums))
                return
            if count >= 4:
                return
            if len(curNum) > 0 and int(curNum) > 255:
                return
            if len(curNum) == 0:
                if index < len(s) and curNum != "0":
                    dfs(curNums[:], index + 1, count, curNum + s[index])
            elif len(curNum) < 3:
                if index < len(s) and curNum != "0":
                    dfs(curNums[:], index + 1, count, curNum + s[index])
                dfs(curNums[:] + [curNum], index, count + 1, "")
            else:
                dfs(curNums[:] + [curNum], index, count + 1, "")
        
        dfs([], 0, 0, "")
        return res


x = Solution()

print(x.restoreIpAddresses("010010"))