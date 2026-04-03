# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        merged = None
        for lst in lists:
            merged = self.mergeTwoLists(merged, lst)
        return merged

    def mergeTwoLists(self, listA: Optional[ListNode], listB: Optional[ListNode]) -> Optional[ListNode]:
        if not listA:
            return listB
        if not listB:
            return listA

        dummy = ListNode(-1)
        curr = dummy

        while listA and listB:
            if listA.val <= listB.val:
                curr.next = listA
                listA = listA.next
            else:
                curr.next = listB
                listB = listB.next
            curr = curr.next
        
        if listA:
            curr.next = listA
        elif listB:
            curr.next = listB
        
        return dummy.next