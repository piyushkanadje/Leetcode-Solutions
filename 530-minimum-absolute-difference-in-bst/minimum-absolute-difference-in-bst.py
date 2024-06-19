# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        arr = []

        def dfs(root):
            nonlocal arr
            if not root:
                return 
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        minVal = float('inf')
        for i in range(1, len(arr)):
            minVal = min(minVal, abs(arr[i-1] - arr[i]))
        
        return minVal