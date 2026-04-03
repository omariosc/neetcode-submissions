class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        currL1 = l1
        currL2 = l2
        
        dummy = ListNode(-1)
        result = dummy
        while currL1 or currL2 or carry:
            v1 = currL1.val if currL1 else 0
            v2 = currL2.val if currL2 else 0
            s = v1 + v2 + carry
            carry = s // 10
            s = s % 10
            
            result.next = ListNode(s)
            result = result.next
            
            if currL1: currL1 = currL1.next
            if currL2: currL2 = currL2.next
            
        return dummy.next