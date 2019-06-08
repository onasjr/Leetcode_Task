## 密钥格式化
## 先转换大写并去除“-”， 之后反向查找，如果凑齐k个就加到res前面，最后剩下不足的作为-前面字符

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = list(S.upper().replace("-", ""))
        res = ""
        tmp = ""
        while S:
            if len(tmp) >= K:       # 反向查找，如果凑齐k个就加到res前面
                res = "-" + tmp + res
                tmp = S.pop()
            else:
                tmp = S.pop() + tmp
        return tmp + res
