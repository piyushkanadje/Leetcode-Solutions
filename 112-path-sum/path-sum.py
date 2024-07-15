# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, curr):
            if not root:
                return False
            
            if root.left is None and root.right is None:
                return curr+ root.val == targetSum
            
            curr+=root.val
        
            left = dfs(root.left, curr)
            right = dfs(root.right, curr)

            return left or right
        
        return dfs(root,0)
