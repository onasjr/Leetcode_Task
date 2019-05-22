# 思路：遍历数组得到a，遍历余下数组得到b，在余下数组中寻找0-a-b，返回下标
# 防止重复：比较是否结果ans中是否包含a和b，不包含则保存；包含时分为a与b相等和不等两种情况，相等时查看数字下标，若该结果中不含两个相同数字则不保存
import copy
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for iii in range(len(nums)):
            nums2 = nums[iii+1:]
            for jjj in range(len(nums2)):
                aaa = nums[iii]
                bbb = nums2[jjj]
                ccc = 0 - aaa - bbb
                test = []
                for m in range(len(ans)):
                    if (aaa in ans[m]) and (bbb in ans[m]):
                        if aaa==bbb:
                            index1 = ans[m].index(aaa)
                            ans_copy = copy.copy(ans[m])
                            del ans_copy[index1]
                            if bbb in ans_copy:
                                test.append(1)
                            else:
                                test.append(0)
                        else:
                            test.append(1)
                    else:
                            test.append(0)
                if sum(test)==0 and (ccc in nums[iii + jjj + 1+1:]):
                    ans.append([aaa, bbb, ccc])
        return ans


# nums = [-1, 0, 1, 2, -1, -4]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
sol = Solution()
sol.threeSum(nums)
