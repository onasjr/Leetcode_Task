## 猜数字游戏
## 依次计算相同坐标位A，之后计算含有相同数字个数B

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        B = 0
        ans = ""
        tmp = []
        for i in range(len(guess)):
            tmp.append(guess[i])
        pdb.set_trace()
        for i in range(len(secret)):
            if secret[i] in tmp:
                B += 1
                tmp.remove(secret[i])
            if secret[i] == guess[i]:
                A += 1
        return ans + str(A) + "A" + str(B-A) + "B"
