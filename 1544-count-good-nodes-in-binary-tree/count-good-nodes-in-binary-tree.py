# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = 0

        def dfs(node, maxSofar):
            if not node:
                return 0
            
            left = dfs(node.left, max(maxSofar, node.val))
            right = dfs(node.right, max(maxSofar, node.val))
            ans = left + right

            if node.val >= maxSofar:
                ans+=1
            
            return ans
        return dfs(root, float("-inf"))