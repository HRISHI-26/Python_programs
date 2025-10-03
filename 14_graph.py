class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node_1, node_2):
        if node_1 not in self.adj_list:
            self.adj_list[node_1] = []
        if node_2 not in self.adj_list:
            self.adj_list[node_2] = []
        self.adj_list[node_1].append(node_2)
        self.adj_list[node_2].append(node_1)

    def display(self):
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")


g = Graph()

g.add_node("A")
g.add_node("B")
g.add_node("C")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")

g.display()
