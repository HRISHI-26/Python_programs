class StackUsingQueue:
    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []
    
    def push(self, data):
        self.queue_1.append(data)
        
        while self.queue_1:
            self.queue_2.append(self.queue_1.pop(0))
        
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1
    
    def pop(self):
        if not self.queue_1:
            print("Stack Underflow")
            return
        print(f"Popped: {self.queue_1.pop()}")
    
    def display(self):
        print(f"Stack: {self.queue_1}")

obj = StackUsingQueue()
arr = [1, 2, 3, 4, 5]
for num in arr:
    obj.push(num)
obj.display()
# - - - - - - - - - - - - 
obj.pop()
obj.display()