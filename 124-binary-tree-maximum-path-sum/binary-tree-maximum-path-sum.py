# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        #here we will need to calculate at each node maximum sum can get upto that node without splitting the further
        #Also we want to make sure that any -ve number is coming in the path or not.
        #Here as it mentioned node can come into path at least once not more than that.
        #Means lets say we want to include 9 -10 20 15 20 7 we can not because we are comiing to 20 for 2 times
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            #why max here we are trying to get the maximum if there is -ve number we will need to take 0 and not the negeaive from both right and left  
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right),0)
            curr= root.val + left + right
            #At each node we can take a maximum sum path and check whether it is maximum path sum or not 
            res = max(curr, res)
            # here we are returning max from left and right because we only can get maximum branch from each point and we can not get the both for the node aboce like for the -10 which is above 20 we will tak max whic is 15
            return root.val + max(left, right)

        dfs(root)
        return res