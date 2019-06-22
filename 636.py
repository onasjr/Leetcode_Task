## 函数的独占空间
## 使用栈，start入栈，end出栈并计算时间更新，当stack中存在任务时，所需时间应减去后一个函数耗时
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0]*n
        stack = []
        for s in logs:
            tmp=s.split(':')
            if tmp[1]=='start':
                stack.append([int(tmp[0]),int(tmp[2])])
            else:
            ## end
                temp = stack.pop()
                time = int(tmp[2])-temp[1]+1
                res[temp[0]]+=time
                ## 存在函数嵌套，减去当前函数耗时
                if stack:
                    res[stack[-1][0]]-=time
        return res
