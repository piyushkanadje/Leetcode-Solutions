# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == target and root.right is None and not root.left:
            return None



        def dfs(node, parent=None):
            if not node:
                return
            
            # Traverse the left subtree
            dfs(node.left, node)
            # Traverse the right subtree
            dfs(node.right, node)

            # Check if the current node is the leaf node to be deleted
            if node.val == target and not node.left and not node.right:
                print(f"Deleting leaf node with value: {node.val}")
                if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None

        dfs(root)
        if root.val == target and not root.left and not root.right:
            return None
        return root
