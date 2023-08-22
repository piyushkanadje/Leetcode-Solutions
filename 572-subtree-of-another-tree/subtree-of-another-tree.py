# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            elif (root and subRoot):
                return (root.val == subRoot.val) and sameTree(root.left,subRoot.left) and sameTree(root.right, subRoot.right)
            else:
                return False
        
        return bool(root and subRoot) and  ( sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) )
    
