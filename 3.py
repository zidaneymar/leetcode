class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #brute force
        if not s or not len(s):
            return 0
        res = 1
        ss = str(s)
        for i in range(0, len(ss)):
            store = set()
            store.add(ss[i])
            curMax = 1
            for j in range(i+1, len(ss)):
                if not ss[j] in store:
                    store.add(ss[j])
                    curMax = len(store)
                    res = max(curMax, res)
                else:
                    break
        return res


s = Solution()
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
