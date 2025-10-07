class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return
        print(f"Deleted: {self.stack.pop()}")
    
    def display(self):
        print(f"Stack: {self.stack[::-1]}")

obj = Stack()
arr = [4, 3, 5, 2, 6, 9]

for num in arr:
    obj.push(num)
obj.display()
# ======================
obj.pop()
obj.display()