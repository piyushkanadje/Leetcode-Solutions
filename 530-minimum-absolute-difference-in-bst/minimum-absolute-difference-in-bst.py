# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minVal= float('inf')
        self.previouNode = None
        def dfs(root):
            if not root:
                return 

            dfs(root.left)
            if self.previouNode is not None:
                self.minVal= min(self.minVal, abs(root.val - self.previouNode.val))
            self.previouNode = root
            dfs(root.right)

            return self.minVal
        
        return dfs(root)
