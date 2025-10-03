class Stack:
    def __init__(self) -> None:
        self.queue_1 = []
        self.queue_2 = []

    def push(self, data):
        self.queue_1.append(data)

        while self.queue_1:
            self.queue_2.append(self.queue_1.pop(0))

        self.queue_1, self.queue_2 = self.queue_2, self.queue_1

    def pop(self):
        print(f"Deleted: {self.queue_1.pop()}")

    def display(self):
        print(f"Stack: {self.queue_1[::-1]}")


obj = Stack()
# - - - - - - - - -
arr = [1, 4, 3, 2, 5]
for num in arr:
    obj.push(num)
# - - - - - - - - -
obj.display()
# - - - - - - - - -
obj.pop()
# - - - - - - - - -
obj.display()
