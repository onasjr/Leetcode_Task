## 键盘行
## 比较第一个字符存在的行中是否包含所有字符

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dict1 = 'QWERTYUIOPqwertyuiop'
        dict2 = 'ASDFGHJKLasdfghjkl'
        dict3 = 'ZXCVBNMzxcvbnm'
        A = []
        for i in words:
            A.append(i)
            tmp = list(i)
            if tmp[0] in dict1:
                for j in tmp:
                    if dict1.find(j) == -1:
                        A.pop()
                        break
            elif tmp[0] in dict2:
                for j in tmp:
                    if dict2.find(j) == -1:
                        A.pop()
                        break
            elif tmp[0] in dict3:
                for j in tmp:
                    if dict3.find(j) == -1:
                        A.pop()
                        break
        return A                    
                    
