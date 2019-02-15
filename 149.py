# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class SameGradientSet:
    def __init__(self, pointNumDict):
        self.gradients = set()
        self.pointNumDict = pointNumDict
    def __len__(self):
        sum = 0
        for p in self.gradients:
            sum += self.pointNumDict[p]
        return sum
    def add(self, p):
        self.gradients.add((p.x, p.y))
    def has(self, p):
        return (p.x, p.y) in self.gradients

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        maxPoint = 0
        pointNum = {}
        pointWithoutDuplicates = []
        for p in points:
            if (p.x, p.y) not in pointNum:
                pointNum[(p.x, p.y)] = 1
                pointWithoutDuplicates.append(p)
            else:
                pointNum[(p.x, p.y)] += 1
            maxPoint = max(maxPoint, pointNum[(p.x, p.y)])
        
        gradientDict = {}



        for p1 in pointWithoutDuplicates:
            for p2 in pointWithoutDuplicates:
                x1, x2, y1, y2 = p1.x, p2.x, p1.y, p2.y
                g = None
                if x1 == x2:
                    g = float('inf')
                else:
                    g = (y1 - y2) / (x1 - x2)
                if g not in gradientDict:
                    newSet = SameGradientSet(pointNum)
                    newSet.add(p1)
                    newSet.add(p2)
                    gradientDict[g] = [newSet]
                else:
                    succ = False
                    for singleSet in gradientDict[g]:
                        if singleSet.has(p1) or singleSet.has(p2):
                            singleSet.add(p1)
                            singleSet.add(p2)
                            succ = True
                            break
                    if not succ:
                        newSet = SameGradientSet(pointNum)
                        newSet.add(p1)
                        newSet.add(p2)
                        gradientDict[g].append(newSet)
                
                for singleSet in gradientDict[g]:
                    maxPoint = max(maxPoint, len(singleSet))
        return maxPoint

x = Solution()
a = Point(1,1)
b = Point(3,2)
c = Point(5,3)
e = Point(4,1)
f = Point(2,3)
g = Point(1,4)

print(x.maxPoints())
                            