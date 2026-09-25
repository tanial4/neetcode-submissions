# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        currentA = headA
        currentB = headB

        while currentA is not currentB:
            currentA = currentA.next if currentA else headB
            currentB = currentB.next if currentB else headA
        
        return currentA
        