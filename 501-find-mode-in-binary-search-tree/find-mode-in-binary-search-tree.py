# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict = {}
        if not root:
            return 0
        queue = []
        queue.append(root)
        while queue:
            curr = queue.pop()
            dict[curr.val] = 1 + dict.get(curr.val,0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        value = max(dict.values())
        ans =[]
        for key in dict.keys():
            if dict[key] == value:
                ans.append(key)
        return ans





        