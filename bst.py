from collections import Container
from queue import Queue, PriorityQueue


class BinarySearchTree (Container):
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def __iter__(self):
            return iter((self.left, self.right))
        
    

    def __init__(self, *items):
        self.root = None
        for item in items:
            self.add(item)

        
    def __contains__(self, item):
        raise NotImplementedError()
 
    def __iter__(self):
        return (node.value for node in self.inorder_traversal())

    def inorder_traversal(self):
        def inorder_iter(current):
            if current:
                yield from inorder_iter(current.left)
                yield current
                yield from inorder_iter(current.right)
        return inorder_iter(self.root)

    def depth_traversal(self):
        def depth_iter():
            stack = []
            if self.root: stack.append(self.root) 
            
            while len(stack) != 0:
                node = stack.pop()
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                
                yield node
        return depth_iter()

    def get_height(self):
        def get_height_recursive(node, height):
            if not node: return height
            
            return max(
                get_height_recursive(node.left, height+1), 
                get_height_recursive(node.right, height+1))
            
        return get_height_recursive(self.root, 0)

    def breath_traversal(self):
        def breath_iter():
            q = Queue()
            if self.root: q.put(self.root) 
            
            while not q.empty():
                node = q.get()
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
                    
                yield node
        return breath_iter()

    def dfs(self, item):
        for node in depth_traversal():
            if node.value == item:
                return node
        return None

    def bfs(self, item):
        for node in breath_traversal():
            if node.value == item:
                return node
        return None

    def add(self, item):
        if not self.root: 
            self.root = BinarySearchTree.Node(item)
            return

        isLeft = False
        parent, current = None, self.root
        while current:
            if item < current.value:
                parent, current = current, current.left
                isLeft = True
            else:
                parent, current = current, current.right
                isLeft = False
            
        if isLeft:
            parent.left = BinarySearchTree.Node(item)
        else: 
            parent.right = BinarySearchTree.Node(item)

    def remove(self, item):
        if not self.root: 
            return None

        parent, current = None, self.root
        while current is not None and current.value != item:
            if item < current.value:
                parent, current = current, current.left
            else:
                parent, current = current, current.right

        return parent

def my_print(*args, sep=' ', end='\n'):
    import sys
    sys.stdout.write(f"{sep.join(args)}{end}")