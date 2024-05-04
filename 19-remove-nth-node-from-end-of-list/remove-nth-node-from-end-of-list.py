# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count +=1
            curr = curr.next

        if count == 1 :
            return None
        if count == n:
            head = head.next
            return head 
        count = count - n -1
        temp = head
        while count > 0:
            temp = temp.next
            count-=1
        
        if temp.next:
            temp2 = temp.next
            temp.next = temp2.next
        
        return head