## 
## 计算C中字符在S中的位置并组成index；对于0~len(S)-1 分别计算和index中位置的距离
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index = [i for i,j in enumerate(S) if j == C]
        return [min([abs(i-j) for j in index]) for i in range(len(S))]
