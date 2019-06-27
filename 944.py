## 删列造序
## 将字符串按列比较，是否呈顺序排列，若不是则res+1表示删除该列
## 使用zip函数按列打包为元组

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        # 按索引值打包成一个元组（一列）
        for i in zip(*A):
            if list(i) != sorted(i):
                res += 1
        return res
