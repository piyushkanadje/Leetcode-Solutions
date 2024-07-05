# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head.next
        newNode = ListNode(0)
        prev= newNode
        while node:
            summ = 0
            while node.val!=0:
                summ+=node.val
                node = node.next
            newNode.next = ListNode(summ)
            newNode= newNode.next
            node =node.next
        return prev.next
