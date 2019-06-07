## 字符串中的查找与替换
## 先对indexes进行排序，之后检查相对坐标位是否相等，替换后更新检查到的坐标数

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        # sort by indexes
        sorted_indexes = sorted(range(len(indexes)), key=lambda k: indexes[k])
        indexes = [indexes[i] for i in sorted_indexes]
        sources = [sources[i] for i in sorted_indexes]
        targets = [targets[i] for i in sorted_indexes]

        T = []
        last_pos = 0    # 上次替换的尾坐标
        for i, start in enumerate(indexes):
            src, tgt = sources[i], targets[i]
            src_len = len(src)
            if S[start:start + src_len] == src: # start:开始比较为相同的坐标
                T.append(S[last_pos:start]) # 替换坐标之前
                T.append(tgt)   # 替换坐标之后
                last_pos = start + src_len
        T.append(S[last_pos:])
        return ''.join(T)
