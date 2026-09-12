class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = self.addNode(self.root, key, val)

    def addNode(self, root, key, val):
        if not root:
            return TreeNode(key, val)
        
        if key < root.key:
            root.left = self.addNode(root.left, key, val)
        elif key > root.key:
            root.right = self.addNode(root.right, key, val)
        else:
            root.val = val
        return root

    def get(self, key: int) -> int:
        return self.binarySearch(self.root, key)
        
    def binarySearch(self, root, key):
        if not root:
            return -1
        if root.key == key:
            return root.val
        if key < root.key:
            return self.binarySearch(root.left, key)
        else:
            return self.binarySearch(root.right, key)

    def getMin(self) -> int:
        minimum = self.findMinimum(self.root)
        return minimum.val if minimum != -1 else -1

    def findMinimum(self, root):
        if not root:
            return -1
        
        current = root
        while current.left:
            current = current.left
        return current

    def getMax(self) -> int:
        if not self.root:
            return -1
        
        current = self.root
        while current.right:
            current = current.right
        return current.val

    def remove(self, key: int) -> None:
        self.root = self.deleteNode(self.root, key)

    def deleteNode(self, root, key):
        if not root:
            return None
        if key < root.key:
            root.left = self.deleteNode(root.left, key)
        elif key > root.key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.findMinimum(root.right)
                root.key = minNode.key
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.key)
        return root

    def getInorderKeys(self) -> List[int]:
        arr = []
        self.dfs(self.root, arr)
        return arr
    
    def dfs(self, root, arr):
        if not root:
            return
        self.dfs(root.left, arr)
        arr.append(root.key)
        self.dfs(root.right, arr)


class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None