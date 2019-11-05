# the key point is: the mid is always inside the left node,

# and left/right node have no intersection




class SegmentTreeNode():
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum
        self.left = None
        self.right = None
    

def build(start, end, nums):
    if start > end:
        return
    
    root = SegmentTreeNode(start, end, 0)

    if start != end:
        mid = start + (end - start) // 2
        
        root.left = build(start, mid, nums)
        root.right = build(mid + 1, end, nums)
        
        root.sum = root.left.sum + root.right.sum

    else:
        root.sum = nums[start]
    
    return root


def query(root, start, end):
    # try to get the sum between start and end
    if root.start == start and root.end == end:
        return root.sum
    
    mid = root.start + (root.end - root.start) // 2

    if end <= mid:
        return query(root.left, start, end)
    elif start >= mid + 1:
        return query(root.right, start, end)
    elif start < mid + 1 and end > mid:
        return query(root.left, start, mid) + query(root.right, mid + 1, end)

def modify(root, index, val):
    if root.start == index == root.end:
        root.sum = val
        return

    mid = root.start + (root.end - root.start) // 2

    if index <= mid:
        modify(root.left, index, val)
    elif index > mid:
        modify(root.right, index, val)

    root.sum = root.left.sum + root.right.sum

    


nums = [0,1,2,3,4]
root = build(0, len(nums) - 1, nums)


for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        print(query(root, i, j))

modify(root, 4, 15)
for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        print(query(root, i, j))