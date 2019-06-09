## 组合综合②
## 迭代时从下一位开始，最后删除重复项

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        res = []

        def eachTime(candidates, target, start, ans, res):
            if start > len(candidates):
                return
            if start == len(candidates):
                if target == 0:
                    tmp = ans[:]
                    res.append(tmp)
                else:
                    return
            for i in range(start, len(candidates)):
                if target > 0:
                    ans.append(candidates[i])
                    eachTime(candidates, target-candidates[i], i+1, ans, res)
                    ans.pop()
                elif target == 0:
                    tmp = ans[:]
                    res.append(tmp)
                    return
        eachTime(candidates, target, 0, ans, res)
        list = []
        for i in res:
            if not i in list:
                list.append(i)
        return list
