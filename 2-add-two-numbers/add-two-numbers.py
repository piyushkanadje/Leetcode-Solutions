# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        carry = 0
        curr = dummy
        while l1!=None or l2!=None or carry == 1:
            sum = 0
        #Here we are checking because we have different size linkedlist
            if l1!=None:
                sum += l1.val
                l1 = l1.next
            if l2!=None:
                sum +=l2.val
                l2= l2.next
        
        #we have to add carry in the 
            sum+=carry
        #Recalculate the carru
            carry = sum//10
            node = ListNode(sum%10)
        #First curr was pointing to None (dummy)
            curr.next = node
        #here we want it to be node which will be helpful to have a new node
            curr = curr.next
        
        return dummy.next

        
        