## 划分字母区间
## 1. 用dict记录字母出现的最后位置
## 2. 从前往后遍历，双指针，start为子序列开始，end为S[start]出现的最后位置，在子序列中查找每个字母的最后位置，更新end

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lll = len(S)
        if lll == 0:
            return []

        res = []
        dict = {}
        # 存放出现的最后坐标位置
        for i in range(lll):
            dict[S[i]] = i

        start = 0
        end = dict[S[start]]
        # 在start和end之间查找字出现的最后位置，如果大于当前的end，则更新end
        while end < lll:
            i = start
            while i < end:
                if dict[S[i]] > end:
                    end = dict[S[i]]
                i += 1
            res.append(end-start+1)
            start = end + 1

            if start >= lll:
                return res
            else:
                end = dict[S[start]]

        return res
