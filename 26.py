## 逆遍历，删除相同项中的下标大的一个
class Solution(object):
    def removeDuplicates(self, nums):
        tmp=len(nums)-1
        while tmp > 0:
            if(nums[tmp]==nums[tmp-1]):
                nums.remove(nums[tmp])
            tmp-=1
        return len(nums)


nums = [1,1,2,2,3,1,1,5,5,6]
ans = Solution().removeDuplicates(nums)
print(ans)
