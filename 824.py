## 山羊拉丁文
# 转为list， 分情况

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        tmp = S.split()
        for i, char in enumerate(tmp):
            # 首字母为元音
            if char[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                tmp[i] = char + 'ma' + 'a'*(i+1)
            else:
                # 首字母为辅音
                tmp[i] = char[1:] + char[0] + 'ma' + 'a'*(i+1)
        return ' '.join(tmp)
