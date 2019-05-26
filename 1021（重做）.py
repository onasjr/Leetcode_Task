## 删除最外层的括号
## 建立栈，通过（与）数量应相同寻找闭合子序列，取中间部分

class Solution:
    def removeOuterParentheses(self, S):
        stack = []
        result= ""
        temp =""
        for c in S:
            temp += c       # 当前分解后的每一部分
            if c == '(':        # 判断是否为闭合子括号序列
                stack.append(c)
            else :
                stack.pop()
            if len(stack) == 0:     # 闭合时栈为空，取中间部分
                result += temp[1:-1]
                temp=""
        return result
