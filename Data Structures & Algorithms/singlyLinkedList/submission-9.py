class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        current = self.head.tail
        pos = 0
        while current:
            if pos == index:
                return current.value
            current = current.tail
            pos += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.tail = self.head.tail
        self.head.tail = node

        if self.tail == self.head:
            self.tail = node


    def insertTail(self, val: int) -> None:
        node = Node(val)
        self.tail.tail = node
        self.tail = node

    def remove(self, index: int) -> bool:
        if not self.head.tail:
            return False
        if index == 0:
            if self.head.tail == self.tail:
                self.tail = self.head
            self.head.tail = self.head.tail.tail
            return True
        
        pos = 0
        current = self.head
        while pos < index:
            current = current.tail
            pos += 1
        
        if current and current.tail:
            if current.tail == self.tail:
                self.tail = current
            current.tail = current.tail.tail
            return True

        return False

    def getValues(self) -> List[int]:
        if not self.head.tail:
            return []
        current = self.head.tail
        arr = [current.value]
        while current.tail:
            current = current.tail
            arr.append(current.value)
        return arr
        
class Node:
    def __init__(self, value: int):
        self.value = value
        self.tail = None