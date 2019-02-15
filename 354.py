
class Solution:
    
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        if len(envelopes) == 0:
            return 0
        
        envelopes.sort(key = lambda x : (x[0], -x[1]))
        


        dp = []
        new_env = []
        prev = None
        for i in range(0, len(envelopes)):
            if not prev:
                new_env.append(envelopes[i])
            else:
                if prev != envelopes[i]:
                    new_env.append(envelopes[i])
            prev = envelopes[i]
        envelopes = new_env
        
        def binarySearch(dp, val):
            low = 0
            high = len(dp) - 1
            res = None
            while low <= high:
                mid = (low + high) // 2
                if dp[mid] == val:
                    res = mid
                    break
                if val > dp[mid]:
                    low = mid + 1
                else:
                    high = mid - 1          

            if res:
                for i in range(res, len(dp) - 1):
                    if dp[i] != dp[i + 1]:
                        return i + 1 

            return low

        
        
        dp.append(envelopes[0][1])
        
        for i in range(1, len(envelopes)):
            index = binarySearch(dp, envelopes[i][1])
            if index < len(dp):
                if index > 0 and envelopes[i][1] > dp[index - 1]:
                    dp[index] = envelopes[i][1]
                elif index == 0:
                    dp[index] = envelopes[i][1]
            else:
                dp.append(envelopes[i][1])
                

        return len(dp)

x = Solution()
print(x.maxEnvelopes([[13,13],[13,13],[17,2],[13,11],[4,6],[7,7],[10,3],[1,3],[20,18],[11,2],[8,7],[1,13],[4,16],[14,16],[2,10],[1,14],[5,7],[3,12],[2,16]]))