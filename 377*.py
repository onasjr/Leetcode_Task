## 组合总和 Ⅳ

## 递归（超时）
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = []
        res = []
        l = len(nums)
        if target == 0:
            if 0 in nums:
                return 1
            else:
                return 0
        def eachTime(all, target, ans, res):
            for i in range(l):
                if all < target:
                    ans.append(nums[i])
                    eachTime(all + nums[i], target, ans, res)
                    ans.pop()
                elif all == target:
                    tmp = copy.copy(ans)
                    res.append(tmp)
                    return

        eachTime(0, target, ans, res)
        # pdb.set_trace()
        return len(res)
        
## dp  dp[i] = dp[i-num] + dp[i]
将i分为num和dp[i-num]

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or min(nums) > target:
            return 0
        nums.sort()
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in range(target + 1):
            for v in nums:
                if v > i:
                    break
                dp[i] += dp[i-v]
        return dp[target]
