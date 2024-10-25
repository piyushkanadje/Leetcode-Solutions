# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 and node2:
                return False
            elif node1 and not node2:
                return False
            elif node1.val != node2.val:
                return False
        
            left1 = node1.left
            right1 = node1.right
            left2 = node2.left
            right2 = node2.right
            
            return (dfs(left1, right2)and dfs(left2, right1)) or (dfs(left1, left2) and dfs(right1, right2))
        return dfs(root1, root2)
