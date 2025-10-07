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
    
    def reverse(self, string):
        rev = []
        self.stack = []
        
        for ch in string:
            self.push(ch)
            
        while self.stack:
            rev.append(self.stack.pop())
            
        newstring = "".join(rev)
        print(f"Reverse: {newstring}")

obj = Stack()
arr = [5, 3, 6, 2, 6]
for num in arr:
    obj.push(num)
obj.display()
# =====================
obj.reverse("helloworld!")