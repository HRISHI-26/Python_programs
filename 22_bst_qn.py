# Implement a BST and perform the following:
# 1.  Insert the numbers: [50, 30, 70, 20, 40, 60, 80, 10, 35, 45].
# 2.  Find the second-largest element in the BST without converting it to a list.
# 3.  Check if the BST is a valid BST after insertion.
# 4.  Print all nodes at a given level (e.g., level 3).

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if root.data < data:
            if not root.left:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        elif root.data > data:
            if not root.right:
                root.right = Node(data)
            else:
                self._insert(root.right, data)
    
    def display(self, node=None, level=0):
        if not node:
            node = self.root
        if node.left:
            self.display(node.left, level+1)
        print("  " * level + str(node.data))
        if  node.right:
            self.display(node.right, level+1)
    
    def secondlargest(self):
        if not self.root:
            return None
        parent = None
        current = self.root
        while current.left:
            parent = current
            current = current.left
        
        return parent.data
    
    def print_level(self, node, level):
        if not node:
            return
        if level == 1:
            print(node.data, end=" ")
        elif level > 1:
            self.print_level(node.left, level - 1)
            self.print_level(node.right, level - 1)


bst = BST()
arr = [40, 39, 58, 30, 67, 20, 2090]

for num in arr:
    bst.insert(num)
bst.display()
# ===================================
print(f"Second Largest:  {bst.secondlargest()}")
# ===================================
bst.print_level(bst.root,3)