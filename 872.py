## 深度优先搜索
## eachroot函数传入当前子支和已有叶子节点数组，只有当该子支不存在左右子支即为叶子节点时append nums

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        nums1 = []
        nums2 = []
        
        def eachroot(root, nums):
            if root and not root.left and not root.right:
                nums.append(root.val)
            if root.left:
                eachroot(root.left, nums)
            if root.right:
                eachroot(root.right, nums)
            return nums
        
        return eachroot(root1, nums1) == eachroot(root2, nums2)
