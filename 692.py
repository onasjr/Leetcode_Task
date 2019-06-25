## 前k个高频单词
## 用dict记录单词出现顺序

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # 存放单词及出现次数
        dict = {}
        for i in words:
            dict[i] = dict.get(i, 0) + 1
        num = sorted(dict.values(), reverse = True)[k-1]  # 第k个所对应的出现次数
        
        # 存放出现次数大于k的单词及次数
        dict2 = {}
        for i,v in dict.items():
            if v >= num:
                dict2[i] = dict2.get(i, 0) + v
        # 按照出现次数对每个次数中的单词按字母顺序排列
        maxk = max(dict2.values())
        mink = min(dict2.values())
        ans = [list() for i in range(maxk-mink+1)]
        for i, v in dict2.items():
            ans[maxk-v].append(i)

        res = []
        for i in ans:
            i.sort()
            res.extend(i)
        return res[:k]
