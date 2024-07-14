# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue=[]
        queue.append(root)
        level =0
        while queue:
            queueLen= len(queue)
            currn = float("-inf") if level %2 ==0 else float('inf')

            for _ in range(queueLen):
                node = queue.pop(0)
                if level %2 ==0:
                    if node.val %2==0 or node.val <= currn:
                        return False
                if level %2 !=0 :
                    if node.val %2 !=0 or node.val >= currn:
                        return False
                currn = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        
        return True
