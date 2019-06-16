## 朋友圈
## 建立visited记录这个人是否被查找过相关关系，递归遍历相关的朋友圈


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        len_m = len(M)
        visited = [0 for i in range(len_m)]
        friend_count = 0
        
        ## 查找第i个人相关的朋友圈，相关联的人在vistied中记为1
        def dfs(M,i,visited,len_m):
            visited[i] = 1
            for j in range(len_m):
                if M[i][j] == 1 and visited[j] == 0:
                    dfs(M,j,visited,len_m)
            
        for i in range(len_m):
            if visited[i] == 0:     # 当第i个人未被查找过，调用dfs，并给个数加一
                friend_count += 1
                dfs(M,i,visited,len_m)
        return friend_count
