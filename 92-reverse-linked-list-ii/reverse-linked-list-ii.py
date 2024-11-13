# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        prev = dummy

        for i in range(left -1):
            prev= prev.next
        
        curr = prev.next
    
        for i in range(right - left):
            next_element = curr.next
            curr.next = next_element.next
            next_element.next = prev.next
            prev.next = next_element
    
        return dummy.next
            
