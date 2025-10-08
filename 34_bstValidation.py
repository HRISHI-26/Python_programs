class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BstValidation:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, root, data):
        if data < root.data:
            if root.left:
                self._insert(root.left, data)
            else:
                root.left = Node(data)
        elif data > root.data:
            if root.right:
                self._insert(root.right, data)
            else:
                root.right = Node(data)

    def delete(self, root, key):
        if not root:
            return root
        
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root
                
    
    def display(self, node=None, level=0):
        if not node:
            node = self.root
            
        if node.left:
            self.display(node.left, level+1)
        print("  " * level + str(node.data))
        if node.right:
            self.display(node.right, level+1)
    
    def validate(self, root, min_val=float('-inf'), max_val=float('inf')):
        if not root:
            return True
        if not (min_val < root.data < max_val):
            return False
        return (self.validate(root.left, min_val, root.data) and 
                self.validate(root.right, root.data, max_val))

        
obj = BstValidation()

arr = [4, 5, 4, 3, 2, 5, 6, 3]

for num in arr:
    obj.insert(num)

obj.display()
# - - - - - - - - - - - - - - - - - 
print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
obj.delete(obj.root, 3)
obj.display()
# - - - - - - - - - - - - - - - - - 
print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
print(obj.validate(obj.root))
