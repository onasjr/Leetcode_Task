## 用 Rand7() 实现 Rand10()
## 扩展等概率空间，rand7() - 1产生0-6，(rand7()-1)*7产生（0-6）*7，因此可扩展到0-48，取其中0-39，/10取余+1

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            tmp = (rand7()-1)*7 + rand7() - 1
            if tmp < 40:
                return tmp % 10 + 1
