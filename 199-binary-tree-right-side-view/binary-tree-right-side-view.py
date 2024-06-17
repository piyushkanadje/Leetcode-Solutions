# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        ans = []
        queue=[]
        queue.append(root)

        while queue:
            nodeInqueue= len(queue)
            count = 0
            for i in range(nodeInqueue):
                node = queue.pop(0)
                count+=1
                if count == nodeInqueue:
                    ans.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
                
