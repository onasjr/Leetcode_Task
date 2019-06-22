## 分数加减运算
## 寻找分母最小公倍数，统一，计算扩倍后的分子和，再计算分子分母最大公约数，化简

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        # 将分母统一，计算分子，之后寻找最大公约数化简# 最大公约数
        def gcd(a, b):
            # if a < b :
            #     a, b = b, a
            if a % b == 0:
                return b
            else:
                return gcd(b, a % b)

        ## 最小公倍数
        def lcm(a, b):
            zdgys = gcd(a, b)
            return int(a * b // zdgys)

        if expression.count('/') == 1: return expression
        expression = expression.replace('-', '+-')
        tmp = expression.split('+')
        ans = []
        for i in tmp:
            if len(i):
                y = i.split("/")
                ans.append((int(y[0]), int(y[1])))
        fm, fz = 1, 0
        for i in ans:
            fm = lcm(fm, i[1])
        for i in ans:
            fz += i[0]*(fm//i[1])
        if fz == 0:
            return "0/1"
        zdgys = gcd(fm, abs(fz))
        return str(fz//zdgys)+"/"+str(fm//zdgys)
