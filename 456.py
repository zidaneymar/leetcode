class Solution:
    def find132pattern(self, nums) -> bool:
        stack = []
        m = []
        curM = float('inf')
        for n in nums:
            if n < curM:
                m.append(n)
                curM = n
            else:
                m.append(curM)
                
                
        for i in reversed(range(0, len(nums))):
            
            while len(stack) != 0 and m[i] >= stack[-1]:
                stack.pop()

            if len(stack) > 0 and m[i] < stack[-1] < nums[i]:
                return True
            
            if len(stack) == 0 or stack[-1] > m[i]:
                stack.append(nums[i])
            
           
        return False

print(Solution().find132pattern([3,5,0,3,4]))