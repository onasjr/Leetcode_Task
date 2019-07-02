## 查询后的偶数和
# 

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # 建立ans存放每次查询后的偶数和
        ans = [0 for _ in range(len(queries))]
        # 初始化ans[0]为查询前的偶数和
        ans[0] = sum([i for i in A if i % 2 == 0])
        
        # 遍历请求数组
        for i in range(len(queries)):
            tmp = ans[i]
            # 若改动数字原先为偶数，分为改动值偶数奇数
            if A[queries[i][1]] % 2 == 0:
                if queries[i][0] % 2 == 0:
                    ans[i] = tmp+queries[i][0]
                else:
                    ans[i] = tmp-A[queries[i][1]]
            # 若改动数字原先奇数，分为改动值奇数和偶数
            else:
                if queries[i][0] % 2 == 0:
                    ans[i] = tmp
                else:
                    ans[i] = tmp+queries[i][0]+A[queries[i][1]]
            A[queries[i][1]] += queries[i][0]
            
            if i <= len(queries)-2:
                ans[i+1] = ans[i]
        return ans
