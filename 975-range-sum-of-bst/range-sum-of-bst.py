# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        def dfs(root):
            nonlocal summ

            if not root:
                return 0
            if root.val >= low and root.val<=high:
                summ+=root.val
            dfs(root.left)
            dfs(root.right)

            return summ

        return dfs(root)