# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: list):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        res = []
        before = None
        for _inter in intervals:
            if not before:
                before = _inter
                res.append(_inter)
            else:
                if _inter.start <= before.end:
                    res.remove(before)
                    cur = Interval(before.start, max(_inter.end, before.end))
                    res.append(cur)
                    before = cur
                else:
                    res.append(_inter)
                    before = _inter
            
        return res


x = Solution()
print(x.merge([Interval(1, 3), Interval(2, 6), Interval(8,10), Interval(15,18)]))