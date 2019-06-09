## 全排列
## 递归，设全局变量ans和res，参数为每次用过数据删除后的list，直到list中为空


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        res = []

        def eachTime(candidate, ans, res):
            # pdb.set_trace()
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
                return res
        aaa = eachTime(nums, ans, res)
        return res
