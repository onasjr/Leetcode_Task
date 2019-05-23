## 相同的树
## 思路：如果两棵二叉树rootl 、root2 相等，那么rootl 与root2 结点的值相同，同时它们的左右分支也有着相同的结构，
# 并且对应位置上结点的值相等。
## 1.分几种p和qTreeNode是否为空及节点是否相同的情况，在节点相同的情况下比较左右分支，递归调用

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        elif p.val != q.val:
            return False
        else:
            left_flag = self.isSameTree(p.left, q.left)
            right_flag = self.isSameTree(p.right, q.right)
            return left_flag and right_flag
