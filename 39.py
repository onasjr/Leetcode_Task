## 组合总和
## 递归调用，每次在后i个序列中寻找组合，当target>0时迭代

class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        ans = []
        res = []

        def eachTime(candidates, target, start, ans, res):
            for i in range(start, len(candidates)):
                if target > 0:
                    ans.append(candidates[i])
                    eachTime(candidates, target-candidates[i], i, ans, res)
                    ans.pop()
                elif target == 0:
                    tmp = ans[:]
                    res.append(tmp)
                    return
        eachTime(candidates, target, 0, ans, res)
        return res
