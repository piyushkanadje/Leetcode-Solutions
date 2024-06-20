# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        width =0

        queue= []
        queue.append((root, 0))
        while queue:
            queuelength = len(queue)
            _, levelOfRoot = queue[0]
            for i in range(queuelength):
                node, parentRoot = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2* parentRoot))
                if node.right:
                    queue.append((node.right, 2*parentRoot + 1))
            width = max(width, parentRoot - levelOfRoot + 1)
        
        return width