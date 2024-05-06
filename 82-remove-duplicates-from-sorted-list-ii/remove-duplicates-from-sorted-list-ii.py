# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy.next
        val = set()
        while curr:
            if (curr.next and curr.val == curr.next.val) or curr.val in val:
                prev.next = curr.next
                val.add(curr.val)
            else:
                prev = curr
            curr = curr.next
        return dummy.next