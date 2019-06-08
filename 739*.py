## 每日温度
## 建立栈，将T中数据和索引依次入栈，与当前位置比较，使当前元素比栈顶元素大时，栈顶出栈，并记录栈顶与当前元素索引差值


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0]*len(T)
        for i,v  in enumerate(T):
            while stack and stack[-1][1] < v:
                t = stack.pop()
                res[t[0]] = i - t[0]
            stack.append((i, v))
        return res
