## 寻找最长前缀
## 依次取第一个str的前i位，比较其他str中前i位是否相同；若相同则存入ans，继续加一位；不同或不存在则return上一次ans

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        flag = []
        strs = sorted(strs)
        # pdb.set_trace()
        num = len(strs)
        if num > 1:
            for i in range(len(strs[0])):
                # pdb.set_trace()
                tmp = strs[0][:i+1]
                m = num - 1
                while m >= 1:
                    if tmp == strs[m][:i+1]:
                        flag.append(0)
                    else:
                        flag.append(1)
                        break
                    m -= 1
                if sum(flag) == 0:
                    ans = strs[0][:i+1]
            return ans
        elif num == 1:
            return strs[0]
        else:
            return ""
