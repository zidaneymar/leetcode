# private int search(int[] bit, int i) {
#     int sum = 0;
    
#     while (i < bit.length) {
#         sum += bit[i];
#         i += i & -i;
#     }

#     return sum;
# }

# private void insert(int[] bit, int i) {
#     while (i > 0) {
#         bit[i] += 1;
#         i -= i & -i;
#     }
# }

class BinaryIndexTree:
    def __init__(self, nums):
        self.nums = nums
    
    def search(self, i):
        res = 0
        while i < self.nums[i]:
            res += self.nums[i]
            i += i & - i
        return res
    
    def insert(self, i):
        while i > 0:
            self.nums[i] += 1
            i -= i & -i
    

nums = [1,3,2,3,1]
tree = BinaryIndexTree([0] * len(nums))


tree.insert(1)

tree.search(0)