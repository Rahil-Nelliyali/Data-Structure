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

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]
            for vertices in self.graph.values():
                if node in vertices:
                    vertices.remove(node)

    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            if node2 in self.graph[node1]:
                self.graph[node1].remove(node2)
                self.graph[node2].remove(node1)

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

    def is_connected(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            visited = set()
            stack = [node1]

            while stack:
                node = stack.pop()
                if node == node2:
                    return True
                if node not in visited:
                    visited.add(node)
                    stack.extend(self.graph[node])

        return False

    def get_neighbors(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            return []

    def shortest_distance(self, start_node, target_node):
        if start_node == target_node:
            return 0

        visited = set()
        queue = [(start_node, 0)]
        front = 0

        while front < len(queue):
            node, distance_in = queue[front]
            front += 1

            if node == target_node:
                return distance_in

            if node not in visited:
                visited.add(node)
                neighbors_in = self.graph[node]
                for neighbor in neighbors_in:
                    queue.append((neighbor, distance_in + 1))

        return -1


# Example usage:
graph = Graph()

# Add nodes
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_node("G")
graph.add_node("H")

# Add edges
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")
graph.add_edge("E", "A")
graph.add_edge("F", "C")
graph.add_edge("G", "A")
graph.add_edge("H", "A")

# Remove a node and an edge
# graph.remove_node("C")
# graph.remove_edge("A", "B")

# Traverse the graph using BFS
print("BFS traversal:")
graph.traverse_bfs("A")

# Traverse the graph using DFS
print("DFS traversal:")
graph.traverse_dfs("A")

# Get neighbors of a node
neighbors = graph.get_neighbors("A")
print("Neighbors of A:", neighbors)

# Check if two nodes are connected
connected = graph.is_connected("C", "A")
print("C and A are connected:", connected)

# Find the shortest distance
distance = graph.shortest_distance("A", "C")
if distance != -1:
    print("Shortest distance between A and C:", distance)
else:
    print("There is no path between A and C.")