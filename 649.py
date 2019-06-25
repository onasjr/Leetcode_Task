## Dota2参议院
## 递归，传入目前轮到第i位发言，以及剩余数组，类似圆桌问题

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        ## 递归，传入目前轮到第i位发言，剩余数组
        def eachTime(index, lastnums):
            lll = len(lastnums)
            if index >= lll:
                index = 0
            if "R" not in lastnums:
                return "Dire"
            elif "D" not in lastnums:
                return "Radiant"
            now = index+1
            while now < index + lll:
                newnow = now % lll
                if lastnums[newnow] != lastnums[index]:
                    lastnums = lastnums[:newnow]+lastnums[newnow+1:]
                    return eachTime(index+1, lastnums)
                else:
                    now += 1
        return eachTime(0, senate)
