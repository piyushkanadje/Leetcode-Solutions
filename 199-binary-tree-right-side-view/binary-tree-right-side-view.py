# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        array = []

        def dfs(root, array, level):
            if not root:
                return
            
            if len(array) == level:
                array.append(root.val)
            
            dfs(root.right, array, level+1)
            dfs(root.left, array, level+1)

            return root
        
        dfs(root,array,0)
        return array


            
        