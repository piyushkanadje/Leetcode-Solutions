# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        self.string =""
        def dfs(root):
            if not root:
             
                return 
            self.string+="("
            self.string+=str(root.val)
            if not root.left and root.right:
                self.string+=str("()")
            dfs(root.left)
            dfs(root.right)
            self.string+=')'
        dfs(root)
        return self.string[1:-1]