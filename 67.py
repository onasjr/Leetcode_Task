## 二进制求和
## 转10进制

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_int = int(a, 2)
        b_int = int(b, 2)
        # pdb.set_trace()
        sum_ab = a_int + b_int
        ab = bin(sum_ab)
        return ab[2:]
