## 比较版本号
## 按.分割为list，将每个字符转化为int（去掉前导0）
## 在后面补齐0，比较两个list大小

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(j) for j in version2.split('.')]
        m = max(len(v1), len(v2))
        v1.extend([0] * (m - len(v1)))
        v2.extend([0] * (m - len(v2)))
        if v1 > v2:
            return 1
        elif v2 > v1:
            return -1
        else:
            return 0
