class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        print(f"{self.data}", end=" ")
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()

    def insert(self, data):
        if not self.left:
            self.left = BinaryTree(data)
        elif not self.right:
            self.right = BinaryTree(data)
        else:
            self.left.insert(data)
    
root = BinaryTree("A")
arr = ["B", "C", "D", "E"]

for char in arr:
    root.insert(char)
root.inorder()