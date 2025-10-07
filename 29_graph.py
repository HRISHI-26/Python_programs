class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []
    
    def add_edge(self, node_1, node_2, directed=False):
        if node_1 not in self.adj_list:
            self.adj_list[node_1] = []
        if node_2 not in self.adj_list:
            self.adj_list[node_2] = []
        self.adj_list[node_1].append(node_2)
        if not directed:
            self.adj_list[node_2].append(node_1)
    
    
    def remove_node(self, node):
        for connection in self.adj_list[node]:
            self.adj_list[connection].remove(node)
        
        del self.adj_list[node]
        
    
    def display(self):
        for node in self.adj_list:
            print(f"{node}: {self.adj_list[node]}")


obj = Graph()
# ============================
obj.add_node("A")
obj.add_node("B")
obj.add_node("C")
obj.add_node("D")
# ============================
obj.add_edge("A", "B")
obj.add_edge("A", "C")
obj.add_edge("A", "D")
obj.add_edge("B", "C")
obj.add_edge("B", "D")
obj.add_edge("C", "D")

obj.display()
# ============================
print("- - - - - - - - - - - - -")
# ============================
obj.remove_node("B")
obj.display()
# ============================
