


# lower bound
def LowerBound(num: list, start: int, end: int, target: int):
    while start < end:
        mid = start + (end - start) // 2
        if num[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def UpperBound(num: list, start: int, end: int, target: int):
    while start < end:
        mid = start + (end - start) // 2
        if num[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start

TestNum = [1,2,5,6,7,8,12,15,16,17]
print(LowerBound(TestNum, 0, len(TestNum), 8))
print(UpperBound(TestNum, 0, len(TestNum), 8))