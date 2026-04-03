class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node = Node(value)
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = Node(value)
        first = self.head.next

        first.prev = node
        node.next = first
        node.prev = self.head
        self.head.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        last = self.tail.prev
        prev = last.prev
        prev.next = self.tail
        self.tail.prev = prev

        return last.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        first = self.head.next
        next_node = first.next

        self.head.next = next_node
        next_node.prev = self.head
        return first.val
        

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None