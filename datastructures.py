from collections.abc import Collection

class LinkedList (Collection):
    class Node (object):
        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

    def __init__(self, *i):
        # reserved start of linked list
        self.root = LinkedList.Node(None)
        self.end = self.root        

        count = 0
        # initialize with iterable
        for n in i:
            self.end.next = LinkedList.Node(n)
            self.end = self.end.next
            count += 1

        self.end.next = self.root

        self._len = count

        def _node_iter():
            curr = self.root.next
            while curr != self.root:
                yield curr
                curr = curr.next
        self._node_iter = _node_iter


    def __iter__(self):
        return (n.value for n in self._node_iter())

    def __getitem__(self, idx):
        if not -len(self)+1 <= idx < len(self):
            raise IndexError()

        idx = (idx + len(self)) % len(self)

        n = iter(self)
        for _ in range(idx-1):
            next(n)
        return next(n)
            
        
    def __setitem__(self, idx, value):
        if not -len(self)+1 <= idx < len(self):
            raise IndexError()

        idx = (idx + len(self)) % len(self)

        node_iter = self._node_iter()
        for _ in range(idx-1):
            next(node_iter)
        
        next(node_iter).value = value

    def __len__(self):
        return self._len

    def __contains__(self, v):
        return v in iter(self)

    def __eq__(self, ll):
        if len(ll) != len(self): return False
        return all((a == b for a,b in zip(iter(self), iter(ll))))

    def __str__(self):
        return "[{}]".format(", ".join((str(v) for v in self)))

    def append(self, value):
        self.end.next = LinkedList.Node(value)
        self.end = self.end.next
        self.end.next = self.root
        self._len += 1

    # TODO: prob can make better
    def extend(self, iterable):
        for i in iterable:
            self.append(i)

    def insert(self, idx, value):
        new_node = LinkedList.Node(value)

        node_iter = self._node_iter()
        for _ in range(idx-1): next(node_iter)
        tgt_node = next(node_iter)
        new_node.next = tgt_node.next
        tgt_node.next = new_node

        if tgt_node is self.end: 
            self.end = self.end.next
        self._len += 1

    def remove(self, value):
        node_iter = self._node_iter()
        
        prev_node = self.root
        for n in node_iter:
            if n == value:
                prev_node.next = n.next
            prev_node = n    
            break

        self._len -= 1


    def pop(self, idx=-1):
        if len(self) <= 0: raise IndexError()

        node_iter = self._node_iter()

        last = None
        secound_last = None
        for _ in range( (idx + len(self)) % len(self) ):
            secound_last = last
            last=next(node_iter)
       
        self.end = secound_last
        secound_last.next = self.root
        self._len -= 1

        return last

    def clear(self):
        self.root.next = self.root
        self._len = 0
    
    def index(self, value, start=0, end=-1):
        end = (end + len(self)) % len(self)
        
        values = iter(self)
        for _ in range(start):
            next(values)
        
        idx = start
        for _ in range(end - start):
            if value == next(values): return idx
            idx += 1

        return -1

    def count(self, value):
        c = 0
        for v in self:
            if v == value: c += 1
        
        return c

    def copy(self):
        return LinkedList(*self)
    
# Contaiment vs Iheritance
class Stack:
    def __init__(self, *i, container_type=list):
        self.container = container_type()
        self.container.extend(i)
        
    def pop(self):
        return self.container.pop()
        
    def push(self, item):
        self.container.append(item)

    def peak(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0
    
    def __str__(self):
        return str(self.container)

def solve_RPN_eval(expr, type=float):
    rpn_stack = Stack()
    expr = expr.split()

    for o in expr:
        try:
            type(o)
            rpn_stack.push(o) 
        except ValueError:
            rpn_stack.push(str(eval( rpn_stack.pop() + o + rpn_stack.pop() )))   
        return rpn_stack.pop()
def solve_RPN_func_map(expr):
    func_map = {
        '+' : lambda x, y : x +  y,
        '-' : lambda x, y : x -  y,
        '/' : lambda x, y : x /  y,
        '//': lambda x, y : x // y,
        '*' : lambda x, y : x *  y,
        '**': lambda x, y : x ** y
    }
    
    rpn_stack = Stack()
    expr = expr.split()

    for o in expr:
        if o in func_map.keys():
            rpn_stack.push(func_map[o](rpn_stack.pop(), rpn_stack.pop()))
        
        else:
            rpn_stack.push(float(o))
    
    return rpn_stack.pop()

def fib():
    # 0, 0, 1, 1, 2,...
    yield 0
    last, current = 0, 1

    while True:
        yield last
        last, current = current, current + last





