# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans =[]

        if not root: return
        queue = []
        queue.append(root)

        while queue:
            level = []
            length = len(queue)
            for i in range(length):
                ele = queue.pop(0)
                level.append(ele.val)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            ans.append(level)
        
        lastRow = len(ans) -1
        return ans[lastRow][0]
