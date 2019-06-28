## 最近的请求次数
## 队列队尾进队首出的特性


from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.queue = deque()
        
    ## 在一次调用中计算3s内调用ping的次数
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        
        while(self.queue[0] < t - 3000):
            self.queue.popleft()
            
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
