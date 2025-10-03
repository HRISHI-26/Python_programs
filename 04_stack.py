class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            print(f"Stack Underflow")
            return
        print(f"Deleted: {self.stack.pop()}")

    def peek(self):
        print(self.stack[-1])

    def display(self):
        print(f"Stack: {self.stack[::-1]}")


# - - - - - - - - - - - -
obj = Stack()
# - - - - - - - - - - - -
arr = [1, 3, 2, 5, 4]
for num in arr:
    obj.push(num)
# - - - - - - - - - - - -
obj.display()
# - - - - - - - - - - - -
obj.peek()
# - - - - - - - - - - - -
obj.pop()
obj.display()
# - - - - - - - - - - - -
