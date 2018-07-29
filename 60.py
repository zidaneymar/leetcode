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

        n_list = [i for i in range(1, n + 1)]
        
        res = ""
        def calNthNumber(n_list: list, k):
            nonlocal res
            if len(n_list) == 0:
                return            
            total = fac[len(n_list)]
            n = len(n_list)
            next_n_index = int(k / (total / n))
            next_n = n_list[next_n_index]
            res += str(next_n)
            next_n_list = n_list[0:next_n_index] + n_list[next_n_index+1:] 
            calNthNumber(next_n_list, k % (total / n))

        calNthNumber(n_list, k - 1)
        return res


x = Solution()
print(x.getPermutation(4, 9))