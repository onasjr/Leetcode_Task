## 复写零
# 

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        tmp = []
        lll = len(arr)
        
        # 遍历该数组
        while i < lll:
            # 将连续0保存在tmp中
            if arr[i] == 0:
                tmp.append(arr[i])
                i += 1
            else:
                # 当出现连续0时，在该位置插入tmp
                if tmp != []:
                    arr = (arr[:i] + tmp + arr[i+len(tmp)-1:])[:lll]
                    i += len(tmp)
                    tmp = []
                else:
                    i += 1
        # pdb.set_trace()
        return
