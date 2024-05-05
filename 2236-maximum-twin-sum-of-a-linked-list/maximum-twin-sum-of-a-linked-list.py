# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast= head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        sum_pairs = 0
        first_half = head
        second_half = prev  # Reversed second half
        maxVal = 0
        while first_half and second_half:
            sum_pairs = first_half.val + second_half.val
            maxVal = max(maxVal, sum_pairs)
            first_half = first_half.next
            second_half = second_half.next
        return maxVal
