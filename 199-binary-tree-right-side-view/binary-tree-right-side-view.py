# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = []
        queue.append(root)
        ans = []
        while queue:
            curr_len= len(queue)
            ans.append(queue[-1].val)

            for _ in range(curr_len):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        return ans