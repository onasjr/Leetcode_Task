## 最少移动次数使数组元素相等 II
## 思路：通过分析，最小移动次数为使每一项变为中位数，因此对奇数偶数分情况讨论


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        if l <= 1:
            return 0
        
        ans = []
        if l % 2 == 0:
            tmp1, tmp2 = 0, 0
            for i in nums:
                tmp1 += abs(i-nums[l//2])
                tmp2 += abs(i-nums[l//2-1])
            ans.append(tmp1)
            ans.append(tmp2)
        else:
            tmp = 0
            for i in nums:
                tmp += abs(i-nums[l//2])
            ans.append(tmp)
        return min(ans)
