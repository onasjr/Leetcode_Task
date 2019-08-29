遍历字符串，对字母对应的数字求和，超过100，计数加1。最后剩下没超过100的，放到最后一行。

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        base=ord('a')
        sums,count=0,0
        for s in S:
            ints=widths[ord(s)-base]
            sums+=ints
            if sums>100:
                count+=1
                sums=ints
        return [count+1,sums]
