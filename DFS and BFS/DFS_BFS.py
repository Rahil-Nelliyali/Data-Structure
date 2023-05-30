class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def traverse_bfs(self, start_node):
        visited = set()
        queue = [start_node]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node)
                visited.add(node)
                queue.extend(self.graph[node])

    def traverse_dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()

        print(start_node)
        visited.add(start_node)

        for neighbor in self.graph[start_node]:
            if neighbor not in visited:
                self.traverse_dfs(neighbor, visited)


# Example usage:
graph = Graph()

# Add nodes
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")

# Add edges
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")

# Traverse the graph using BFS
print("BFS traversal:")
graph.traverse_bfs("A")

# Traverse the graph using DFS
print("DFS traversal:")
graph.traverse_dfs("A")
