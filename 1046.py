## 最后一块石头的重量
## 递归


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        def eachTime(stones):
            # 对石头从小到大排序
            stones.sort()
            # 当只剩下一个石头或无石头时得出结果停止迭代
            if len(stones) <= 1:
                return stones[0] if stones != [] else 0
            else:
                # 当最后两个石头满足前一个小于后一个，则将两个石块出栈并重新加入差值
                if stones[-2] < stones[-1]:
                    newstone = stones[-1] - stones[-2]
                    stones.pop()
                    stones.pop()
                    stones.append(newstone)
                else:
                # 当二者相同，则栈顶弹出两次
                    stones.pop()
                    stones.pop()
                return eachTime(stones)

        return eachTime(stones)
