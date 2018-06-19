class Solution:
    def longestCommonPrefix(self, strs: list):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        cur = None
        minLen = float("inf")
        if strs == [] or not strs:
            return res
        for s in strs:
            minLen = min(len(s), minLen)
        for i in range(0, minLen):
            check = ""
            isValid = True
            for s in strs:
                if check == "":
                    check = s[i]
                else:
                    isValid = check == s[i]
                    if not isValid:
                        break
            if not isValid:
                return res
            else:
                res += check
        return res

s = Solution()
print(s.longestCommonPrefix(["a", "abc"]))