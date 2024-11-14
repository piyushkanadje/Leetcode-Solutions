# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)   
        prev = dummy
        curr = head
        s =[]
        while curr and curr.next:
            if curr.val == curr.next.val:
                s.append(curr.val)
            curr= curr.next

        curr_head  = head

        while curr_head:
            while curr_head and curr_head.val in s:
                curr_head= curr_head.next
            
            prev.next = curr_head
            prev = curr_head
            if curr_head:
                curr_head= curr_head.next
        
        return dummy.next
            
                