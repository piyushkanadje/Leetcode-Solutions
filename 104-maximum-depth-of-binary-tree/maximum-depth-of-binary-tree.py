# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is  None:
            return 0
        queue= deque()
        queue.append(root)
        level= 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left is not None:
                    queue.append(curr.left)    
                if curr.right is not None:
                    queue.append(curr.right)
            level += 1
        
        return level
        