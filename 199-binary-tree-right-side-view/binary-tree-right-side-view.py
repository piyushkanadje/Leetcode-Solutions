# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr =[]
        def dfs(root, level, arr):
            if not root:
                return
            
            if len(arr) == level:
                arr.append(root.val)
            
            dfs(root.right, level+1,arr)
            dfs(root.left, level+1, arr)

            return root
        
        dfs(root,0,arr)
        return arr