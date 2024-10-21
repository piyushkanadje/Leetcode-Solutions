# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(root, minn, maxx):
            nonlocal result
            if not root:
                return 0

            result = max(abs(maxx- root.val), abs(minn - root.val), result)
            minn = min(minn, root.val)
            maxx = max(maxx, root.val)
            dfs(root.left, minn, maxx)
            dfs(root.right,minn, maxx)

        dfs(root, root.val, root.val)

        return result

