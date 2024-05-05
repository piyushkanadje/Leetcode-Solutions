# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev ,curr = dummy, head

        while curr and curr.next:
            #get next pair and the second node to reverse it
            nextPair = curr.next.next
            second = curr.next

            #now reverse 
            second.next = curr
            curr.next = nextPair
            prev.next = second

            #update the pointer
            prev = curr
            curr =nextPair

        return dummy.next