class Permutation:
    def __init__(self, nums):
        self.nums = nums

    def Next(self):
        
        # find the j where nums[j] < nums[j + 1]

        # and find the k where nums[j] < nums[k]

        # swap and reverse nums[j + 1:]
        j = None
        for i in reversed(range(1, len(self.nums))):
            if self.nums[i] > self.nums[i-1]:
                j = i - 1
                break
    
        if j == None:
            return []

        for i in reversed(range(j+1, len(self.nums))):
            if self.nums[i] > self.nums[j]:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
                return self.nums[:j+1] + list(reversed(self.nums[j+1:]))
        return []

    def AllPermutations(self):
        res = []
        self.nums.sort()
        res.append(self.nums[:])
        j = self.Next()

        while len(j) > 0:
            res.append(j[:])
            self.nums = j
            j = self.Next()
        return res




print(Permutation([1,2,3,4]).Next())
