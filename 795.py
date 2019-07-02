## 区间子数组个数
# ans1和ans2分别存储截止到第i位的符合条件子数组个数

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        lll = len(A)
        # ans1和ans2分别存储截止到第i位的符合条件子数组个数
        ans1 = [0 for _ in range(lll)]
        ans2 = [0 for _ in range(lll)]
        
        if A[0] <= R:
            ans1[0] = 1
            k1 = 0
        else:
            k1 = 1
        
        if A[0] < L:
            ans2[0] = 1
            k2 = 0
        else:
            k2 = 1

        for i in range(1, lll):
            # ans1计算max<=R
            if A[i] <= R:
                ans1[i] = i - k1 + 1
            else:
                k1 = i+1
                
            # ans2计算max<L
            if A[i] < L:
                ans2[i] = i - k2 + 1
            else:
                k2 = i+1
        return sum(ans1) - sum(ans2)
