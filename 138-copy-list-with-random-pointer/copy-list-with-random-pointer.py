"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict = {None:None}
        curr = head
        while curr !=None:
            copy =Node(curr.val)
            dict[curr] = copy
            curr = curr.next
        
        curr2 = head
        while curr2 != None:
            copy = dict[curr2]
            copy.next = dict[curr2.next]
            copy.random = dict[curr2.random]
            curr2= curr2.next
        
        return dict[head]