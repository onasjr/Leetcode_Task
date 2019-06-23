## 单词替换
## 按dict顺序遍历，查找nums中单词前len(词根）位是否与词根相同，替换

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        nums = sentence.split(" ")

        # 按dict顺序遍历，查找nums中单词前len位是否与词根相同，替换
        for i in dict:
            lll = len(i)
            for j in range(len(nums)):
                if i == nums[j][0:lll]:
                    nums[j] = i

        return " ".join(nums)
