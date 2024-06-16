# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1, leaf2 = [], []
        def dfs(root, leaf):
            if not root:
                return
            dfs(root.left, leaf)
            if not root.left and not root.right:
                leaf.append(root.val)
            dfs(root.right, leaf)
        
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        return leaf1 == leaf2
        