"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : return None

        queue= deque([node])

        clones = {node.val : Node(node.val,[])}

        while queue:
            curr_node = queue.popleft()
            #getting the curr_clone -> which is current node which we have poped
            curr_clones= clones[curr_node.val]

            for neigh in curr_node.neighbors:
                if neigh.val not in clones:
                    #Adding new node in the clones
                    clones[neigh.val] = Node(neigh.val, [])
                    queue.append(neigh)
                #If node already present addong the full node form the clonds clones[neigh.val] shows the full node whic include Node(va, neig)
                curr_clones.neighbors.append(clones[neigh.val])
            
        return clones[node.val]