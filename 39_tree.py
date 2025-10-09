class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def delete_child(self, value):
        for child in self.children:
            if child.data == value:
                self.children.remove(child)
                return True
            if child.delete_child(child):
                return True
        return False
    
    def display(self, level=0):
        print("  " * level * 2 + str(self.data))
        for child in self.children:
            child.display(level+1)


root = Tree("10")
a = Tree("20")
b = Tree("30")
c = Tree("40")
d = Tree("50")
e = Tree("60")
f = Tree("70")

root.add_child(a)
root.add_child(b)

a.add_child(c)
a.add_child(d)

b.add_child(e)
b.add_child(f)

root.display()