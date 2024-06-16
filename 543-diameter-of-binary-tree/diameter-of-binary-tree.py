# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righ
        if not root:
            return 0
        
        result =0
        def dfs(root):
            if not root:
                return 0
            nonlocal result
            left = dfs(root.left)
            right = dfs(root.right)
            result = max(left+right, result)
            return 1+ max(left, right)
        dfs(root)
        return result