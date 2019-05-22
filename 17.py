## 电话号码的字母组合
## 思路：
## 1. 建立dict表 2. 分别将字符串中每个字符对应的可能结果保存在ans[i]中 3. 遍历数字个数，更新res结果的同时计算i+j的值

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        res = []
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        # pdb.set_trace()
        i = 0
        for num in digits:
            ans.append([x for x in dict[num]])
            if i == 0:
                res = copy.copy(ans[i])
            else:
                res = [(x + y) for x in res for y in ans[i]]
            i += 1
        return res
