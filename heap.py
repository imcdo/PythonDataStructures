

# l = [*[1,2,3,4], 5]
# h= Heap(*l)
# Heap(1,2,3,4,5)

class Heap:
    def __init__(self, *values, max_heap=True):
        # values = (1,2,3,4,5)
        self.heap = [float('inf')]

        self._compare = (lambda x, y : x > y) if max_heap else (lambda x, y : y > x)
        self._group_oper = min if max_heap else max

        for val in values: 
            self.put(val)


    def put(self, val):
        idx = len(self.heap)
        self.heap.append(val)

        parent = Heap._get_parent(idx)

        while  self._compare(self.heap[idx], self.heap[parent]):
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx, parent = parent, Heap._get_parent(parent)

    def get(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        result = self.heap.pop()

        parent = 1
        c1, c2 = Heap._get_children(parent)

        # while min(self.heap[parent], self.heap[c1], self.heap[c2]) != self.heap[parent]:
        while self._group_oper(parent, c1, c2, key= lambda idx : self.heap[idx]) != parent:
            idx = self._group_oper(parent, c1, c2, key= lambda idx : self.heap[idx])
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            parent = idx
            c1, c2 = Heap._get_children(idx)
            
        # FIXME: need a special case when out of bounds


    @staticmethod
    def _get_parent(idx):
        return idx // 2

    @staticmethod
    def _get_children(idx):
        return (idx * 2, idx * 2 + 1)        


    def __contains__(self, val):
        return val in self.heap
