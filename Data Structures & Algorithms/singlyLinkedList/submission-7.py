class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        arr = self.getValues()
        try:
            return arr[index]
        except IndexError:
            return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        
        if not self.head:
            self.head = node
            return
        
        node.tail = self.head
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
        if not index:
            self.head = self.head.tail
            return True
        
        pos = 0
        current = self.head
        while current and pos < index - 1:
            current = current.tail
            pos += 1
        
        if current and current.tail:
            current.tail = current.tail.tail
            return True

        return False

    def getValues(self) -> List[int]:
        if not self.head:
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