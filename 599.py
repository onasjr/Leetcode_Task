## 两个列表的最小索引综合
## =记录两个人喜欢餐厅的索引值，得到共同喜欢的餐厅，查找并记录共同出现的餐厅索引和


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # 记录两个人喜欢餐厅的索引值
        index1 = {list1[i]: i for i in range(len(list1))}
        index2 = {list2[i]: i for i in range(len(list2))}
        # 得到共同喜欢的餐厅
        agreements = set(list1) & set(list2)
        # 查找并记录共同出现的餐厅索引和
        sum_index = {r: index1[r]+index2[r] for r in agreements}
        return [r for r in agreements if sum_index[r] == min(sum_index.values())]
