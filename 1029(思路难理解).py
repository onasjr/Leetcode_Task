## 两地调度
## 按照每个人去a和b的差值从小到大排序，前一半去A，后一半去B

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        lll = len(costs)
        return sum([i[0] for i in costs[:lll//2]]) + sum([i[1] for i in costs[lll//2:]])
