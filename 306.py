class Solution:
    def isAdditiveNumber(self, num: 'str') -> 'bool':
        def dfs(first, target, num):
            if len(num) == 0:
                return True
                
            for j in range(1, len(num) + 1):
                second = int(num[0:j])
                if second != target:
                    continue
                if dfs(second, first + second, num[j:]):
                    return True
            return False
    
        for i in range(1, len(num) + 1):
            first = int(num[0:i])
            if num[0] == '0' and len(num[0:i]) > 1:
                return False
            for j in range(i + 1, len(num) + 1):
                second = int(num[i:j])
                if len(num[i:j]) > 1 and num[i] == '0':
                    break
                if len(num[j:]) > 0 and dfs(second, first + second, num[j:]):
                    return True
        return False


print(Solution().isAdditiveNumber("101"))