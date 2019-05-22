## bin()转10进制为2进制，去掉0b标志，右对齐前面补0到32位
## 翻转二进制字符串

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n_bin = bin(n)[2:].zfill(32)
        n_str_reverse = n_bin[::-1]
        n_reverse = int(n_str_reverse,2)
        return n_reverse
