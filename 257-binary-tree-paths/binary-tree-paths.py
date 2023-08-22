# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def traverse(node, pathTillCurrNode):
            if not (node.left or node.right):
                path.append("->".join(pathTillCurrNode))
                return
            if node.left:
                traverse(node.left, pathTillCurrNode + [str(node.left.val)])
            if node.right:
                traverse(node.right, pathTillCurrNode + [str(node.right.val)])
        
        path = []
        traverse(root, [str(root.val)])
        return path
