## 救生艇
"""
1. 按体重降序排列
2. 双指针l和r计算两个人体重和，若<=限制，船数res+1
3. 不满足，l右移，（因为体重大的优先单人坐船）
"""

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort(reverse = True)
        l, r, res = 0, len(people)-1, 0
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                res += 1
            else:
                l += 1
                res += 1
        if l == r:
            return res + 1
        else:
            return res
