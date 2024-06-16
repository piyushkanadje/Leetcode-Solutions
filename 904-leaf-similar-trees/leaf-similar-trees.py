# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans1 =[]
        ans2=[]
        def dfs1(root):
            nonlocal ans1
            if not root:
                return 0
            
            if root.left == None and root.right == None:
                ans1.append(root.val)
            dfs1(root.left)
            dfs1(root.right)

            return ans1
        def dfs2(root):
            nonlocal ans2
            if not root:
                return 0
            
            if root.left == None and root.right == None:
                ans2.append(root.val)
            dfs2(root.left)
            dfs2(root.right)

            return ans2
        anss1 = dfs1(root1)
        anss2= dfs2(root2)
        print(anss1, anss2)
        return anss1==anss2
        