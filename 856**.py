## 括号的分数
## 栈：栈内为分数，一个括号产生一个分数，根据括号深度叠加分数


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # 栈：栈内为分数，一个括号产生一个分数，根据括号深度叠加分数
        stack = [0]
        for i in S:
            if i == "(":
                stack.append(0)
            else:
                score = stack.pop()
                if score == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2*score
        
        return stack[0]
