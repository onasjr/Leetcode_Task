## 供暖器
## 对heaters排序，找到最接近的位置，更新距离，最后返回最大距离

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        a = []
        c = 0
        heaters.sort()
        for i in houses:
            lll = 0
            rrr = len(heaters) - 1
            while lll <= rrr:
                mid = (lll + rrr) // 2
                if heaters[mid] == i:
                    c = mid
                    break
                elif heaters[mid] < i:
                    lll = mid + 1
                else:
                    rrr = mid - 1
            c = lll
            if c == 0:
                a.append(heaters[0] - i)
            elif c == len(heaters):
                a.append(i - heaters[-1])
            else:
                a.append(min(heaters[c] - i, i - heaters[c-1]))
            c = 0
        return max(a)
                    
