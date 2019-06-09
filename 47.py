## 全排列②
## 递归，从每一位开始调用递归函数，参数为除该元素外的列表
## 最后删除重复项

class Solution(object):
    def permuteUnique(self, nums):
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
        list = []
        for i in res:
            if i not in list:
                list.append(i)
        return list
