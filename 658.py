## 找到k个最接近的元素
## 二分法去掉前后不符合的数

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        ## 二分法，从前后去掉不符合的数
        l, r = 0, len(arr)-1
        while r-l+1 > k:
            dl = abs(arr[l]-x)
            dr = abs(arr[r]-x)
            # 若首位差值>末尾，首位指针向后移动
            if dl > dr:
                l += 1
            else:
                # 若末尾>=首位，末尾指针向前移动
                r -= 1
        return arr[l:r+1]
