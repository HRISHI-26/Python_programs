class Queue:
    def __init__(self) -> None:
        self.stack_1 = []
        self.stack_2 = []

    def enque(self, data):
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())

        self.stack_1.append(data)

        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

    def deque(self):
        if not self.stack_1:
            print("Queue Underflow")
            return
        print(f"Deleted: {self.stack_1.pop(0)}")

    def display(self):
        print(f"Queue: {self.stack_1}")


obj = Queue()
# - - - - - - - -
arr = [3, 2, 4, 1, 5]
for num in arr:
    obj.enque(num)
# - - - - - - - -
obj.display()
# - - - - - - - -
obj.deque()
# - - - - - - - -
obj.display()
