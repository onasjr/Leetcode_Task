## H指数
## 假设引用次数都大于index，若小于则index-1

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        index = len(citations)
        for i in citations:     # 假设引用次数都大于index，若小于则index-1
            if i < index:
                index -= 1
            else:break
        return index
