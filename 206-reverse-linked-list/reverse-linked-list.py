# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head #means curr is not head -> curr is pointing to the head
        prev = None #means prev is not the none its pointing to the none

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        #returnning prev because we are having prev. ==== curr
        return prev


        