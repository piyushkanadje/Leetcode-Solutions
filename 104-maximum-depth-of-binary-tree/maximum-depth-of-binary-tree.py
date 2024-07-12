# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        if not root:
            return 0
        
        def dfs(root):
            if not root:
                return 0
            #here we are writing left and right because we want to use this left and right to get the max of the left or right like in the current node right might be the logest path to maintain which is longest we are assigning the variables.
            left = dfs(root.left)
            right= dfs(root.right)
            return max(left,right) + 1
        
        return dfs(root)