from queue import Queue

# simple node class that we can build a graph out of
class Node:
    class Edge:
        def __init__(self, node, weight=1):
            self.node = node
            self.weight = weight
        
        def __iter__(self):
            return iter((self.node, self.weight))

    def __init__(self, value, neighbors=[]):
        self.value = value
        self._neighbors = list(neighbors)
        
    def add_neighbor(self, neighbor, weight = 1):
        self._neighbors.append(Node.Edge(neighbor))

    def add_neighbor_undirected(self, neighbor, weight = 1):
        self._neighbors.append(Node.Edge(neighbor, weight))
        neighbor._neighbors.append(Node.Edge(self, weight))

    def __iter__(self):
        self._neighbors.sort(key=lambda e : e.weight)
        return (e.node for e in self._neighbors)
    
    def __str__(self):
        return str(self.value)

    def breath_traversal(self):
        visited = set()
        q = Queue()
    
        visited.add(self)
        q.put(self)
        
        while not q.empty():
            current = q.get()
            
            yield current
    
            for neighbor in current:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.put(neighbor)

a = Node("a")
b = Node("b")
c = Node("c")

a.add_neighbor_undirected(b, 10)
a.add_neighbor_undirected(c, 5)
b.add_neighbor_undirected(c, 1)

for neighbor in a:
    print(neighbor)

print("\ntraversal")

for n in a.breath_traversal():
    print(n)


char_list = list((str(n) for n in a.breath_traversal()))
print(f"traversal list: {char_list}\n")

# simple graph class that is easy to use
# downside of this method is no duplicate labels
class Graph:
    def __init__(self):
        self._adj_dict = {}

    def add_item(self, item):
        self._adj_dict.update({item : {}})
    
    def add_directed_edge(self, start, end, weight=1):
        self._adj_dict[start].update({end : weight})

    def add_undirected_edge(self, start, end, weight=1):
        self._adj_dict[start].update({end : weight})
        self._adj_dict[end].update({start : weight})
    
    def plot_graph(self):
        pass

    def __getitem__(self, start):
        return self._adj_dict[start]

    def __str__(self):
        pass


g = Graph()

g.add_item(1)
g.add_item(2)
g.add_item(3)
g.add_undirected_edge(1, 3, 10)
g.add_undirected_edge(1, 2, 20)

print(g[1])
for destination, weight in g[1].items():
    print(f"from 1 to {destination} is weight {weight}")