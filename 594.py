## 最长和谐子序列
## 建立dict保存每个出现数字的次数，查找相差1数字的和

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = []
        a = {}
        # 建立dict保存出现的数字及次数
        for i in nums:
            a[i] = a.get(i,0) + 1
        for i in a:
            if i+1 in a:
                r.append(a[i] + a[i+1])
        if r == []:
            return 0
        return max(r)
