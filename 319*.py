## 灯泡开关
## 直接递归…（超出最大迭代次数）

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        initial = [0]*n

        def eachTime(nums, times , n):
            if times >  n:
                return sum(nums)
            i = times - 1
            while i <= n-1:
                nums[i] = 1 - nums[i]
                i += times
            return eachTime(nums, times+1, n)
        return eachTime(initial, 1, n
        
        
 ### 第i个灯泡的反转次数等于它所有因子（包括1和i）的个数，一开始的状态的灭的，只有反转奇数次才会变成亮的，
 # 所以只有因子个数为奇数的灯泡序号才会亮，只有平方数的因子数为奇数（比如6=1*6,2*3，它们的因子总是成对出现的，而4=1*4,2*2，只有平方数的平方根因子会只出现1次），
 # 所以最终答案等于n以内（包括n和1）的平方数数量，只要计算sqrt(n)即可
 
 ### 用常规列举法试出规律，发现4~8都是亮2个灯泡，9~15都是亮3个灯泡，16~24都是亮4个灯泡，所以规律是sqrt(n)
