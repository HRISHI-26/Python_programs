class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Chain:
    def __init__(self):
        self.root = None
    
    def findkey(self, value):
        self.key = value % 4
        self.value = value
        self.insert()
    
    def insert(self):
        if not self.root:
            node = Node(self.key, self.value)
            self.root = node
            return
        current = self.root
        while current.next:
            current = current.next
        node = Node(self.key, self.value)
        current.next = node
    
    def display(self):
        current = self.root
        while current:
            print(f"{current.key}:{current.value}", end=" -> ")
            current = current.next
        print("Null")


arr = [10, 20, 15, 7, 22]
obj = Chain()

for num in arr:
    obj.findkey(num)

obj.display()