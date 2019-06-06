## 唯一摩尔斯密码词
## 建立dict，遍历，结果存入list，最后使用set返回无重复list
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        Morse_Code_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
        res = []
        for i in range(len(words)):
            tmp = ""
            for j in words[i]:
                tmp += Morse_Code_dict[j]
            res.append(tmp)
        ans = set(res)
        return len(ans)
