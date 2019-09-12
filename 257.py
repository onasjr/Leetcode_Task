## 迭代，维护一个堆栈，将当前路径根节点之外节点记为node，当前根节点及以上根节点记为path，当stack不为空时查看node的left和right支，并更新path路径

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        
        paths = []      # 存放已有路径
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()        # node：当前剩余的树；path：当前树的根节点
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
        
        return paths
