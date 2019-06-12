## 比特位计数
## 找规律，1,2，4,8,等2的倍数是左移得到，因此有相同1的个数
## 其他与该数//2的数字相同+1


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0 for i in range(num+1)]
        for i in range(num+1):
            if i % 2 == 0:
                res[i] = res[i // 2]
            else:
                res[i] = res[i // 2] + 1
        return res
