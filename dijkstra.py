from queue import PriorityQueue

class Node:
    def __init__(self, data, *neighbors):
        self.neighbors = neighbors
        self.data = data

    def __str__(self):
        return str(self.data)
        
def djikstra(start):
    p = PriorityQueue()
    p.put((0,start))

    visited = set()
    path_weights = {start: (0, None)}


    while not p.empty():
        weight_from_start, curr = p.get()
        visited.add(curr)

        for weight, neighbor in filter(lambda x: x[1] not in visited, curr.neighbors):
            new_weight = weight_from_start + weight
            if neighbor not in path_weights.keys() or new_weight < path_weights[neighbor][0]:
                # print(f'node: {hex(id(neighbor))} not in {visited}?')
                assert(neighbor not in visited)

                path_weights.update({neighbor : (new_weight, curr)})
            p.put((new_weight, neighbor))

    for key,value in path_weights.items():
        weight, node = value

        print(f"node {key.data}: {weight}, from {node.data if node is not None else '--'}")


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.neighbors = [(2, b), (3, c)]
b.neighbors = [(1, c), (5, a)]
c.neighbors = [(12, b), (4, a)]
d.neighbors = [(9, c)]

djikstra(d)