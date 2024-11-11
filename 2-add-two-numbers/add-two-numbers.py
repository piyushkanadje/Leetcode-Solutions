# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = l1
        dummy2 = l2
        carry = 0
        newlinked = ListNode()
        curr = newlinked
        while dummy1 and dummy2:
            summ = dummy1.val + dummy2.val + carry
            carry = summ //10
            curr.next = ListNode(summ % 10)
            curr = curr.next
            dummy1 = dummy1.next
            dummy2 = dummy2.next

        while dummy1:
            summ = dummy1.val + carry

            carry = summ //10
            curr.next = ListNode(summ % 10)
            curr = curr.next
            dummy1 = dummy1.next

        while dummy2:
            summ = dummy2.val + carry
            carry = summ //10
            curr.next = ListNode(summ % 10)
            curr = curr.next
            dummy2 = dummy2.next
            

        if carry > 0:
            curr.next = ListNode(carry)
       
        return newlinked.next
