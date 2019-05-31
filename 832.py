## 翻转图像
## 先翻转行，再用全1数组减去

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A = [A[i][::-1] for i in range(len(A))]
        # pdb.set_trace()
        # B = copy.copy(A)
        # B = [[1]*len(A)]*len(A[0])
        ans = []
        for i in range(len(A)):
            tmp = []
            for j in range(len(A[0])):
                tmp.append(1-A[i][j])
            ans.append(tmp)
        return ans
