class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data < root.data:
            if not root.left:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        elif data > root.data:
            if not root.right:
                root.right = Node(data)
            else:
                self._insert(root.right, data)

    def display(self, node=None, level=0):
        if not node:
            node = self.root
        if node.left:
            self.display(node.left, level + 1)
        print(f"{node.data}  ", end=" ")
        if node.right:
            self.display(node.right, level + 1)


bst = BST()

arr = [40, 39, 58, 29, 67]

for num in arr:
    bst.insert(num)

bst.display()
