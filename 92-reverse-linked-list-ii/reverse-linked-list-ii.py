# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None and head.next == None:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        for i in range(left-1):
            prev = prev.next
        #this it the first elementd from the list 
        curr = prev.next

        for i in range(right - left):
            m = curr.next
            curr.next = m.next
            m.next = prev.next
            prev.next = m 
        
        return dummy.next