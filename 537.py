## 复数乘法
## 分别分离实数虚数位

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = 0
        a2 = 0
        b1 = 0
        b2 = 0
        tmp = 0
        if "+" in a:
            tmp = a.index("+")
            # pdb.set_trace()
            a1 = int(a[:tmp])
            a2 = int(a[tmp+1:len(a)-1])
        elif "i" in a:
            a2 = int(a[:-1])
        else:
            a1 = int(a)
        if "+" in b:
            tmp = b.index("+")
            b1 = int(b[:tmp])
            b2 = int(b[tmp+1:len(b)-1])
        elif "i" in b:
            b2 = int(b[:-1])
        else:
            b1 = int(b)
        ans1 = a1*b1 - a2*b2
        ans2 = a1*b2 + a2*b1
        return str(ans1) + "+" + str(ans2) + "i"

## 运用split
    
    class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a, b = a[:-1], b[:-1]
        a1, a2 = a.split("+")
        b1, b2 = b.split("+")
        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
        return str(a1*b1-a2*b2) + "+" + str(a1*b2+a2*b1) + "i"
