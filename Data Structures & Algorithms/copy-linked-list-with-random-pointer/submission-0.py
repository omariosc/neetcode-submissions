"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None: None}
        cur = head
        while cur:
            nodes[cur] = Node(cur.val)
            cur = cur.next

        dummy = Node(-1)
        copy = dummy
        cur = head
        while cur:
            node = nodes[cur]
            copy.next = node
            node.random = nodes.get(cur.random)
            cur = cur.next
            copy = copy.next

        return dummy.next