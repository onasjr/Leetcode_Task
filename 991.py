## 坏了的计算器
## 由y推x——
## 当x>=y: 只能递减得到
## 当x<y： 尽可能使用除法，奇数时加一，偶数时除以2， 最后加上x和y的差值（递减得到）


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y

        count = 0
        while Y > X:
            count += 1
            if Y % 2 == 0:
                Y /= 2
            else:
                Y += 1

        return int(count + abs(Y - X))
