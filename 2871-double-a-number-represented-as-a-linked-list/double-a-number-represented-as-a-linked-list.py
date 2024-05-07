# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr = head
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        temp = prev

        while temp:
            multipy = temp.val * 2 + carry
            carry = multipy//10
            temp.val = multipy % 10
            temp= temp.next   
        
        if carry:
            temp= prev
            while temp.next:
                temp= temp.next
            temp.next = ListNode(carry)
        new = prev
        temp2 = None
        while new:
            nextNode = new.next 
            new.next = temp2
            temp2= new
            new = nextNode
        return temp2
