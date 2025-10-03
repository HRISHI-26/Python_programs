class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return
        print(f"Deleted: {self.stack.pop()}")

    def sortStack(self):
        self.stack_2 = []
        while self.stack:
            temp = self.stack.pop()
            while self.stack_2 and self.stack_2[-1] > temp:
                self.stack.append(self.stack_2.pop())
            self.stack_2.append(temp)

        while self.stack_2:
            self.stack.append(self.stack_2)

        print(self.stack)


arr = [2, 4, 3, 5, 1]
obj = Stack()
for num in arr:
    obj.push(num)
obj.sortStack()
