## 第k个排列（超时）
## 递归产生排列数，对其排序，输出k-1个

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        res = []
        nums = [i for i in range(1,n+1)]

        def eachTime(candidate, ans, res):
            if candidate != []:
                for i in range(len(candidate)):
                    ans.append(candidate[i])
                    tmp = copy.copy(candidate)
                    tmp.remove(candidate[i])
                    eachTime(tmp, ans, res)
                    ans.pop()
            else:
                tmp = copy.copy(ans)
                res.append(tmp)
                return
        eachTime(nums, ans, res)
        # pdb.set_trace()
        res.sort()
        result = ""
        for i in range(n):
            result += str(res[k-1][i])
        return result
