## 加油站
## 1. 若总和gas<cost， 则-1
## 2. 设置一个起始位start，从0开始，在（start， start+len（gas））中遍历，记录每一步之后剩余油量，若<0，则设置start开始位为当前遍历到位置+1，归零剩余量


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        curr = 0
        start = 0
        rest = 0
        for i in range(start, start+len(gas)):
            curr += gas[i%len(gas)]     # 当前站点增加油量
            curr -= cost[i%len(gas)]    # 走到下一个站点消耗之后的油量
            if curr < 0:
                curr = 0
                start = i + 1
        if curr >= 0:
            return start
