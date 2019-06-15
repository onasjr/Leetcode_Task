## 汉明距离总和
## 计算所有位置0和1的数量相乘相加


class Solution(object):
    def totalHammingDistance(self, nums):
        l =[0 for _ in range(32)]       # 存储所有数字每一位含有的1的个数,从末尾开始
        for num in nums:
            aaa = num
            count = 0
            while aaa:
                if aaa&1==1:
                    l[count] = l[count]+1
                count = count+1
                aaa >>=1
        length = len(nums)
        s = 0
        ## 统计所有位置0和1的数量相乘
        for i in l:
            s += (length-i)*i
        return s
