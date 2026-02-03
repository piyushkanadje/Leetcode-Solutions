# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:     
        if head.next==None and n==1:
            return None        
        slow = head
        fast = head 
        dummy = head
        for _ in range(n):
            fast =  fast.next
        if fast==None:
            return slow.next
        while fast:
            dummy = slow
            slow = slow.next
            fast = fast.next
        if dummy.next:
            dummy.next = slow.next
        return head