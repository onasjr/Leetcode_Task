##  最小时间差
## 转化为分钟，计算差值


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time = [0,0]*len(timePoints)
        ans = [0]*len(timePoints)
        for i in range(len(timePoints)):
            time[i] = timePoints[i].split(":")
            if time[i][0] == "00":
                ans[i] = abs(24 * 60 + int(time[i][1]))
            else:
                ans[i] = abs(int(time[i][0]) * 60 + int(time[i][1]))
        ans.sort()
        # pdb.set_trace()
        diff = [float("inf")]
        [diff.append(min(abs(ans[i+1] - ans[i]), abs(24*60-abs(ans[i+1]-ans[i])))) for i in range(len(ans)-1)]
        diff.append(min(abs(ans[0]-ans[-1]), abs(24*60-abs(ans[0]-ans[-1]))))
        return min(diff)
