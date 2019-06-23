## 机器人能否返回原点
## 计算四个方向出现的次数，成对则T

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dict = {"L":0, "R":0, "U":0, "D":0}
        
        for i in moves:
            dict[i] += 1
        if dict["L"] == dict["R"] and dict["U"] == dict["D"]:
            return True
        else:
            return False
