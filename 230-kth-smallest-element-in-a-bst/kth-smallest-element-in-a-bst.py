# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Helper function to perform DFS and find kth smallest element
        def dfs(node):
            nonlocal cnt  # Use nonlocal to update the count variable
            if not node:
                return None

            # Traverse left subtree
            left_result = dfs(node.left)
            if left_result is not None:
                return left_result

            # Update count and check if kth smallest is found
            cnt += 1
            if cnt == k:
                return node.val

            # Traverse right subtree
            return dfs(node.right)

        cnt = 0  # Initialize count
        return dfs(root)
