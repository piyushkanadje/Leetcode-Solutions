# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = []
        queue = []
        queue.append(root)

        while queue:
            nodesInLevel=len(queue)
            level =[]
            for _ in range(nodesInLevel):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        print(ans)
        summ=ans[len(ans)-1]
        return  sum(summ)