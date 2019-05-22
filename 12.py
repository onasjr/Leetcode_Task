## 整数转罗马
## 1. 建立降序数组和dictionary
## 2. 从大到小将数组中的数作为除数，并与dict对应，依次除法

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digit = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        mapping = {1000:"M", 900:"CM", 500:"D",400:"CD", 100:"C", 90: "XC", 50:"L",40: "XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        ans = ""
        for i in digit:
            ans += mapping[i] * (num/i)
            num -= i * (num/i)
            if num == 0:
                break
        return ans
