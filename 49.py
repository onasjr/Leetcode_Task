## 字母异位词分组
## 利用dict，依次将含有相同字母的str放入sorted之后的key中


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for i in strs:
            if str(sorted(i)) not in dict.keys():
                dict[str(sorted(i))] = []
                dict.get(str(sorted(i))).append(i)
            else:
                dict.get(str(sorted(i))).append(i)
        # pdb.set_trace()
        return [i for i in dict.values()]
