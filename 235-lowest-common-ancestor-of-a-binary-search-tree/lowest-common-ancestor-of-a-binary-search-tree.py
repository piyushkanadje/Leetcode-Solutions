# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # this problem can be divided into 3 steps.\
        # if root == left or root== right return root because root always be small
        # if at each point we have left and right then we can return root
        # if we have either we will return that

        if not root:
            return 0
        
        if root ==p or q == root:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right , p, q)

        if left and right:
            return root
        
        if left:
            return left
        
        return right
        
            