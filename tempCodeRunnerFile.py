# Efficient version
class QueueUsingStack:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        self.queue = []
    
    def enque(self, data):
        self.stack_1.append(data)
        self.queue = self.stack_1
    
    def deque(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())

        if not self.stack_2:
            print("Queue Underflow")
            return
        
        self.queue = self.stack_2[::-1] + self.stack_1
        print(f"Deleted: {self.stack_2.pop()}")
    
    def display(self):
        print(f"Queue: {self.queue}")
        

obj = QueueUsingStack()

arr = [1, 2, 3, 4, 5]
for num in arr:
    obj.enque(num)
obj.display()
# =======================
obj.deque()
obj.display()
