# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def reverse(node: Optional(ListNode)):
            curr = node
            prev = None

            while curr:
                nextEle = curr.next
                curr.next = prev
                prev = curr
                curr = nextEle
            
            return prev
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        newHead = reverse(slow)
        ans =0
        while head and newHead:
            ans = max(ans, head.val+newHead.val)
            head = head.next
            newHead= newHead.next


        return ans