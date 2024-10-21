# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right= dfs(root.right)

            return 1+ max(left, right)
        
        height = dfs(root)
        if height==1:
            return root.val

        queue = deque([root])
        count = 0
        ans = 0

        while queue:
            curr_len= len(queue)
            count+=1
            for _ in range(curr_len):
                node = queue.popleft()
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if count==height-1:
                for _ in range(len(queue)):
                    node= queue.popleft()
                    ans+=node.val


        return ans