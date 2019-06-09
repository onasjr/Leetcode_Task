## 组合
## 递归生成子序列，设置全局变量res， ans。
## 达到数字个数时返回

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        res = []
        nums = [i for i in range(1,n+1)]
        # pdb.set_trace()
        ## times: 几个数字
        ## start: 开始遍历位置
        def eachTime(candidate, start, times, ans, res):
            for i in range(start, len(candidate)):
                ans.append(candidate[i])
                eachTime(candidate, i+1, times+1, ans, res)
                ans.pop()
            if times == k:
                tmp = copy.copy(ans)
                res.append(tmp)
                return
        eachTime(nums, 0, 0, ans, res)
        return res
