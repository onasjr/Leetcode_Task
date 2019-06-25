## 棒球比赛
## 分情况，堆栈


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = []
        for i in range(len(ops)):
            if ops[i] == "C":
                ans.pop()
            elif ops[i] == "D":
                ans.append(ans[-1]*2)
            elif ops[i] == "+":
                ans.append(sum(ans[-2:]))
            else:
                ans.append(int(ops[i]))
        
        return sum(ans)
