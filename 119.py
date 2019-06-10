## 杨辉三角②
## 依次生成每一行在r中，每行个数即为行数

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r = [1]
        for i in range(1, rowIndex+1):
            r=[1] + [sum(r[j:j+2]) for j in range(i)] 
        return   r 
