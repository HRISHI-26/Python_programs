class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def delete_child(self, value):
        for child in self.children:
            if child.data == value:
                self.children.remove(child)
                return True
            if child.delete_child(value):
                return True
        return False

    def display(self, level=0):
        print(" " * level * 2 + str(self.data))
        for child in self.children:
            child.display(level + 1)


root = Tree("A")
b = Tree("B")
c = Tree("C")
d = Tree("D")

root.add_child(b)
root.add_child(c)
b.add_child(d)

root.display()
