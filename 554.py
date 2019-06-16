## 砖墙
## 将所有可以组成的长度作为key建立dict，用总层数-去掉首尾的长度values最大值
## 特殊情况，每层只有一块砖

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dict = {}
        ans = ""
        for i in wall:
            ans += str(len(i))
        if ans.count("1") == len(wall) == len(ans):
            return len(wall)
        for i in range(len(wall)):
            alllen = 0
            for lll in wall[i][:-1]:
                alllen += lll
                if alllen != 0:
                    dict[alllen] = dict.get(alllen, 0) + 1
        return len(wall) - max(dict.values())
