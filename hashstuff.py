from datastructures import LinkedList

def double_hash(item):
    hashval = hash(item)
    return hashval * 1093874982384 % 201839578 ^ 103039 

class my_dict:
    def __init__(self, hash_table_size=19):
        self.hash_table = [LinkedList() for _ in range(hash_table_size)]
        
    def insert(self, key, value):
        hashval = hash(key) % len(self.hash_table)
        

        curr = self.hash_table[hashval].root
        self.hash_table[hashval].root.value = (None, None)
        while curr.value[0] != key and curr.next != None:
            curr = curr.next
        if curr.value[0] == key:
            curr.value[1] == value
        else:
            curr.next = LinkedList.Node((key, value))
            self.hash_table[hashval].end = curr.next


    def get(self, key):
        hashval = hash(key) % len(self.hash_table)
        for k, v in self.hash_table[hashval]:
            if key == k:
                return v
        
        return None