## 二进制手表
## 枚举所有数字的对应二进制1个数

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ## 枚举所有可能性1-60中二进制1的个数
        bins = [str(bin(i))[2:].count('1') for i in range(60)]
        results = []
        for hour in range(12):
            for minute in range(60):
                if bins[hour] + bins[minute] == num:
                    results.append('%d:%02d'%(hour, minute))
        return results
        
