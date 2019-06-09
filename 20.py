##有效的括号
## 建立dict对应左右括号，建立栈，左括号入栈，右括号与栈顶的对应括号比较，相同出栈


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {
            "{":"}",
            "[":"]",
            "(":")"
        }

        stack = list()
        for i in range(len(s)):
            # pdb.set_trace()
            if s[i] in dict.keys():
                stack.append(s[i])
            else:
                if stack == []:return False
                elif s[i] == dict[stack[-1]]:
                    stack.pop()
                else:return False
        return stack == []
