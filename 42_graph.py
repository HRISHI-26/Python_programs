class Graph:
    def __init__(self):
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
    
    def remove_node(self, node):
        for connection in self.adj_list[node]:
            self.adj_list[connection].remove(node)
        
        del self.adj_list[node]
        