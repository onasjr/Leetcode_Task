## 柠檬水找零
""" 
分情况：
1. bill == 5:直接加入dict
2. bill == 10：dict[5] -- ,dict[10]++
3. bill == 20：dict[10]-- and dict[5]-- or dict[5]-3
"""

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dict = {5:0, 10:0, 20:0}
        for i in bills:
            dict[i] = dict.get(i, 0) + 1
            if i == 5:
                continue
            elif i == 10:
                if dict[5] -1 >= 0:
                    dict[5] = dict.get(5) - 1
                else:
                    return False
            elif i == 20:
                if dict[10] >= 1 and dict[5] >= 1:
                    dict[5] = dict.get(5) - 1
                    dict[10] = dict.get(10) - 1
                elif dict[5] -3 >= 0:
                    dict[5] = dict.get(5) - 3
                else:
                    return False
        return True
