# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #dummy node for the linkedList
        dummyNode = ListNode(0)
        dummyNode.next = head
        prefixSum = 0
        prefixUntilNode = {0: dummyNode}
        current = head 
        while current:
            prefixSum +=current.val 
            if prefixSum in prefixUntilNode:
                todelete = prefixUntilNode[prefixSum].next
                tempSum = prefixSum + todelete.val
                while todelete != current:
                    del prefixUntilNode[tempSum]
                    todelete = todelete.next
                    tempSum+=todelete.val
                prefixUntilNode[prefixSum].next = current.next
            else:
                prefixUntilNode[prefixSum] = current
            current = current.next
        return dummyNode.next
