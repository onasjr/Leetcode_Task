## K次取反后最大化的数组和
## K次翻转后总和最大——即为每次翻转最小值，循环每次翻转最小值，翻转后重新排序
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        # 每次将最小的值翻转，并重新排序
        while K > 0:
            A.sort()
            A[0] = -A[0]
            K -= 1
        return sum(A)
