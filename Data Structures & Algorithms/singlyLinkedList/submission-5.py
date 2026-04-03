class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        vals = self.getValues()
        try:
            return vals[index]
        except IndexError:
            return -1
        
    def insertHead(self, val: int) -> None:
        temp = self.head
        node = Node(val)
        node.tail = temp
        self.head = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return

        current = self.head
        while current.tail:
            current = current.tail
        current.tail = node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.tail
            return True

        pos = 0
        current = self.head
        while pos < index - 1 and current.tail:
            pos += 1
            current = current.tail
        if current.tail:
            current.tail = current.tail.tail
            return True
        return False

    def getValues(self) -> List[int]:
        if self.head == None:
            return []
        current = self.head
        arr = [current.value]
        while current.tail:
            current = current.tail
            arr.append(current.value)
        return arr

class Node:
    
    def __init__(self, value: int):
        self.value = value
        self.tail = None