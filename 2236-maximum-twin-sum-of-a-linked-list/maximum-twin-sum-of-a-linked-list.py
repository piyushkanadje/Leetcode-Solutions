# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        maximum = 0
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next

        curr = slow 
        prev = None

        while curr: 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr= next_node
        start = head
        while prev:
            maximum = max(maximum, prev.val + start.val)
            start = start.next
            prev= prev.next

        return maximum
            