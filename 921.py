## 使括号有效的最少添加
## 堆栈，当前后满足()时出栈，否则进栈，返回stack长度

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if S == "":
            return 0
        stack = []
        stack.append(S[0])
        for i in S[1:]:
            stack.append(i)
            if len(stack) >= 2 and stack[-2] == "(" and stack[-1] == ")":
                stack.pop()
                stack.pop()

        return len(stack)
                
