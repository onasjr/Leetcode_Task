## 根据身高重建队列
## 1. 按照身高顺序降序排列2.按照前面的人的个数（第二位）插入

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ## 按照身高顺序（第一位）降序排列
        people.sort(key = lambda x: x[1])
        people.sort(key = lambda x: x[0], reverse = True)

        ## 按照前面的人的个数（第二位）插入,比较该同学与前面相比身高高于的数量
        res = []
        for i in people:
            res.insert(i[1], i)
        return res
