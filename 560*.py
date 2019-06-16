## 和为K的子数组

## 不使用数组，遍历，py超时
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lll = len(nums)
        count = 0
        for i in range(lll):
            allsum = 0
            # pdb.set_trace()
            for j in range(i,lll):
                allsum += nums[j]
                if allsum == k:
                    count += 1
        return count
        
        
## 计算从第一位开始的和的出现次数，保存在res中，计算该和s-k是否在rec中，在则count+出现次数。长数组和-前面一部分和

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rec={}
        rec[0]=1#空集-->0
        ans=s=0
        for n in nums:
            s+=n
            if s-k in rec:
                ans+=rec[s-k]
            rec[s]=rec.get(s,0)+1
        return ans
