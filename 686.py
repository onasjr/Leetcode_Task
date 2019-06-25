## 重复叠加字符串匹配
## 如果A比B长，查找2倍A是否存在B；
## 如果B比A长，查找len（B）//len（A）~倍数+1*2 是否包含B

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        n1 = len(B) // len(A)

        if n1 == 0:
            if B in A:
                return 1
            elif B in A*2:
                return 2
            else:
                return -1
        tmp = A * n1
        i = n1
        while i < (n1 + 1) * 2:
            if B in tmp:
                return i
            else:
                i += 1
                tmp += A
        return -1
