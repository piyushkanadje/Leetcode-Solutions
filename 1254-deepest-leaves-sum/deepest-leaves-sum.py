class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        queue = deque()
        queue.append(root)
        maxdepth = 0
        while queue:
            lvllen = len(queue)
            maxdepth += 1
            for i in range(lvllen):
                node = queue.popleft()
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
        
        ans = 0
        
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            lvllen = len(queue)
            depth += 1
            for i in range(lvllen):
                node = queue.popleft()
                if depth == maxdepth:
                    ans += node.val
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
        
        return ans