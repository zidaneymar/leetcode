class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [None] * (n + 1)
        for i in range(0, n + 1):
            if i == 0:
                fac[i] = 1
            else:
                fac[i] = fac[i - 1] * i


        result = []
        def calNthNumber(n, k):
            total = fac[n]
            secondary_n = int(k / (total / n))
            
    
        print(fac)


x = Solution()
print(x.getPermutation(4, 3))