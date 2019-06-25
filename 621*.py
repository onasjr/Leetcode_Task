## 任务调度器

"""
计算每个任务出现的次数
找出出现次数最多的任务，假设出现次数为 x
计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count

特殊情况：
res<len（nums）
"""

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [tasks.count(i) for i in set(tasks)]
        maxcount = max(count)
        mintime = (maxcount-1)*(n+1)
        res = mintime + count.count(maxcount)

        if res < len(tasks):
            return len(tasks)
        else:
            return res
