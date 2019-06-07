## 报数
## 递归，根据上次结果计算下一次（分别保存相同项数字和个数）

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        def next_num(tmp):  # 根据上一次的结果计算下一次
            res = ""
            i = 0
            tmp_n = len(tmp)
            while i < tmp_n:
                count = 1
                while i < tmp_n-1 and tmp[i] == tmp[i+1]:   # 几个重复项
                    count += 1
                    i += 1
                res += str(count)+tmp[i]    # 读两位数字
                i += 1  # 直接从下一位开始重新读数
            return res
        res = "1"
        for i in range(n-1):
            res = next_num(res)
        return res
