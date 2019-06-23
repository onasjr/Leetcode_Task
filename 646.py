## 最长对数链
## 按末位排列，比较当前指针指向数和last中存放的上一个满足条件的数，若满足加入last，否则继续，
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # 按末尾数排列
        pair.sort(key = lambda x:x[1])
        num = 0
        last = -1
        for p in pairs:
            # 从第一个数开始比较
            if last == -1 or p[0] > last[1]:
                num += 1
                last = p
        return num
