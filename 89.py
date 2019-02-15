class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []

        for i in range(0, pow(2, n)):
            res.append(i ^ (i >> 1))

        return res

x = Solution()

print (x.grayCode(2))