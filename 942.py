## 增减字符串匹配
## 从左到右遍历，遇到I则从最小数开始，遇到D则从最大数开始，并依次向内

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i=0
        j=len(S)
        res=[]
        for s in S:
            if s == "I":  #取最小
                res.append(i)
                i+=1
            if s == "D":  #取最大
                res.append(j)
                j-=1
        res.append(i)
        return res
