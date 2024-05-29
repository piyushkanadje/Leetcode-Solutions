# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head,head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)

        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True