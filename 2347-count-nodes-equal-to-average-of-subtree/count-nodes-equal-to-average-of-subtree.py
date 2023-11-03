# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0,0
            leftSubTree = dfs(root.left)
            rightSubTree = dfs(root.right)

            sum = leftSubTree[0] + rightSubTree[0] + root.val
            numberOfNodes = leftSubTree[1] + rightSubTree[1] + 1

            if sum// numberOfNodes == root.val:
                res+=1

            return sum, numberOfNodes
        dfs(root)
        return res
                  


        