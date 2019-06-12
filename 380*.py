## 常数时间插入、删除和获取随机元素
## Hashmap set


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        self.set.add(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            return False
        self.set.remove(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.set:
            return None
        return random.choice(list(self.set))        # 返回列表，元组或字符串中随机一项
