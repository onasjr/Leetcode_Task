## 最小差值①
## 计算最大最小值差值是否在2*K之间，不在则返回max-min-2k；否则0

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if max(A) - min(A) >= 2*K:
            return max(A) - min(A) - 2*K
        else:
            return 0
