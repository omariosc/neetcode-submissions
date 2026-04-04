# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = -1
        i = 0
        seen = {}
        current = head
        while curent:
            if current in seen:
                return seen[current]
            seen[current] = i