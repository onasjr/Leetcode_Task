## 旋转字符串
## 将B拓展一倍，查找A是否在B中

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        # pdb.set_trace()
        B = B*2
        if A in B:
            return True
