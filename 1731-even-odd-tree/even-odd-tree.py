# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isIncreasing(self, arr):
        if len(arr) == 1:
            return arr[0] % 2 != 0  # Should be odd
        for i in range(len(arr) - 1):
            if arr[i] % 2 == 0 or arr[i + 1] % 2 == 0:  # Should be odd
                return False
            if arr[i] >= arr[i + 1]:  # Should be strictly increasing
                return False
        return True

    def isDecreasing(self, arr):
        if len(arr) == 1:
            return arr[0] % 2 == 0  # Should be even
        for i in range(len(arr) - 1):
            if arr[i] % 2 != 0 or arr[i + 1] % 2 != 0:  # Should be even
                return False
            if arr[i] <= arr[i + 1]:  # Should be strictly decreasing
                return False
        return True

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = []
        levelArr = []
        queue.append(root)
        if root.val%2==0:
            return False
        while queue:
            arr = []
            queuLen= len(queue)
            for i in range(queuLen):
                curr = queue.pop(0)
                arr.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            levelArr.append(arr)
            print(arr)
        val=0
        for i in range(len(levelArr)):
            if i % 2==0:
                val= self.isIncreasing(levelArr[i])
                print(val)
                if val == False:
                    return val
            else:
                val= self.isDecreasing(levelArr[i])
                if val == False:
                    return val
        return val


