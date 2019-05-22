
# 思路:先判断给定整数x的正负情况，把符号首先给提取出来,记为flag
# 然后将abs(x)变成字符串，接着将字符串反转，最后恢复成整数
class Solution(object):
    def reverse(self, x):
        """
                :type x: int
                :rtype: int
        """
        if x>=0:flag = 1
        else:flag = -1
        str_x = str(abs(x))
        str_x_reverse = str_x[::-1]
        # pdb.set_trace()
        x_reverse = int(str_x_reverse)
        x_reverse = x_reverse * flag
        if -2**31 < x_reverse< 2**31-1:
            return x_reverse
        else:
            return 0


x = -2147483630
reverse_x = Solution().reverse(x)
print(reverse_x)
