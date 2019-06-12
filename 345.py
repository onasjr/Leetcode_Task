## 反转字符串中的元音字母
## 建立元音字母list，将str转换为list，设置两个指针ij从前后向中间，交换后换回str


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        i  = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i] in nums and s[j] in nums:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in nums:
                i += 1
            elif s[j] not in nums:
                j -= 1
        return "".join(s)
