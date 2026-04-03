# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        while current.next:
            current = current.next
            count += 1
        

        target = count - n + 1
        if target == 0:
            return head.next

        i = 0
        prev = head
        while i < target - 1:
            prev = prev.next
            i += 1
        if prev.next:
            prev.next = prev.next.next
        else:
            prev.next = None
        return head
