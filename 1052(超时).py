## 爱生气的书店老板
# 计算为0的客人总数，之后用滑块计算k范围内不为0总数，取最大值

class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        lll = len(customers)
        if lll <= X:
            return sum(customers)
        maxtmp = 0
        ans = sum([customers[i] for i in range(lll) if grumpy[i] == 0])
        for i in range(lll - X + 1):
            tmp = sum([customers[j+i] for j in range(len(customers[i: i+X])) if grumpy[j+i] == 1])
            maxtmp = max(maxtmp, tmp)
        return ans + maxtmp
