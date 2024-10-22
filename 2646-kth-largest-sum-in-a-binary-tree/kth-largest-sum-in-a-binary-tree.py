# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import insort_left
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        summ = []

        queue = deque([root])

        while queue:
            curr_len= len(queue)
            curr_sum = 0
            for _ in range(curr_len):
                node = queue.popleft()
                curr_sum+=node.val
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            insort_left(summ, curr_sum)
        
        print(summ)
        if len(summ) < k:
            return -1

        return summ[len(summ)-k]
            