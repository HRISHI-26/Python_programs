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
        print("Stack:",self.stack[::-1])
    
    def sort(self):
        self.stack_2 = []
        
        while self.stack:
            temp = self.stack.pop()
            
            while self.stack_2 and self.stack_2[-1] > temp:
                self.stack.append(self.stack_2.pop())
            self.stack_2.append(temp)
        
        while self.stack_2:
            self.stack.append(self.stack_2.pop())


obj = Stack()
arr = [4, 3, 6, 2, 7]
for num in arr:
    obj.push(num)
obj.display()
# ==========================
obj.sort()
obj.display()