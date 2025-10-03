class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BFS:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data < root.data:
            if not root.left:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        elif data > root.data:
            if not root.right:
                root.right = Node(data)
            else:
                self._insert(root.right, data)

    def bfs(self):
        if not self.root:
            return []
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


obj = BFS()

arr = [23, 45, 34, 12, 25]

for num in arr:
    obj.insert(num)
print(obj.bfs())
