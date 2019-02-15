class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        start = 0
        total = 0
        step = 0
        while start < len(gas):
            diff = gas[(start + step) % len(gas)] - \
                cost[(start + step) % len(gas)]
            total += diff
            if total < 0:
                start += step + 1
                step = 0
                total = 0
            else:
                if step == len(gas):
                    return start
                step += 1
        return -1


x = Solution()
print(x.canCompleteCircuit([2,3,4],[3,4,3]))
