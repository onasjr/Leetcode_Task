## 消除游戏
## 设置一个变量表示现在是奇数次还是偶数次，奇数次从0位开始删除；偶数次从末尾开始删除


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        nums = [i for i in range(1, n+1)]
        while len(nums) != 1:
            if i % 2 == 1:
                del nums[0::2]
            else:
                del nums[-1::-2]
            i += 1
        return nums[0]
