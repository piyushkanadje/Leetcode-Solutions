# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue=[]
        queue.append(root)
        count= 0
        while queue:
            nodesInLevel=len(queue)
            level =[]
            count+=1
            for _ in range(nodesInLevel):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if count%2==0:
                ans.append(level[::-1])
            else:
                ans.append(level)
    
        return ans