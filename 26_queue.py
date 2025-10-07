class Queue:
    def __init__(self):
        self.queue = []
    
    def enque(self, data):
        self.queue.append(data)
    
    def deque(self):
        if not self.queue:
            print("Queue Underflow")
            return
        print(f"Deleted: {self.queue.pop(0)}")
    
    def display(self):
        print(f"Queue: {self.queue}")
    
obj = Queue()
arr = [5, 3, 6, 7, 2, 6]

for num in arr:
    obj.enque(num)
obj.display()
# ====================
obj.deque()
obj.display()