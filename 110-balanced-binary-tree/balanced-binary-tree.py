# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if not root:
            return 0
        return 1 + max(self. height(root.left), self.height(root.right))
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        queue= deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            
            left = self.height(node.left)
            right = self.height(node.right)

            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
            
            if (abs(left-right)>1):
                return False
        return True