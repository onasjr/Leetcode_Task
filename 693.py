## 交替位二进制数
## 转换为二进制字符串，查找是否存在00或11

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not ("11" in bin(n) or "00" in bin(n))
