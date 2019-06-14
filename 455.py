## 分发饼干
## 用尽量小的饼干区满足小朋友，满足后将该饼干去除


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        for i in g:
            for j in s:
                if i <= j:
                    count += 1
                    s.remove(j)
                    break
        return count
