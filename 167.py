## 两数之和 2
## 遍历第一个数，在余下数组中查找第二个数是否存在
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in numbers:
            index1 = numbers.index(i)
            if index1 == len(numbers)-1:
                return []
            elif i > target:
                return []
            elif (target-i) in numbers[index1+1:]:
                numbers.index(i)
                return [index1+1, numbers[index1+1:].index(target-i)+index1+2]
        return []
