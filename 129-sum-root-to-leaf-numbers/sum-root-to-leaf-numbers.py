# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = 0
        path = []

        def dfs(node):
            nonlocal path, s
            if not node:
                return

            path.append(str(node.val))  # Convert the node value to a string
            if node.left is None and node.right is None:
                pathSum = ''.join(path)  # Join the path list to form the number
                s += int(pathSum)  # Convert to an integer and add to sum
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()

        dfs(root)
        return s