class Key():
    def __init__(self, key, value = None, next_node = None, prev_node = None):
        self.key = key
        self.prev_node = prev_node
        self.next_node = next_node
        self.value = value
    def set_value(self,value):
        self.value = value
    def get_value(self):
        return self.value
    def get_prev_node(self):
        return self.prev_node
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node
    def set_next_node(self, next_node):
        self.next_node = next_node
    def get_next_node(self):
        return self.next_node
    def get_key(self):
        return self.key
class HashMap():
    def __init__(self):
        self.tail = None
        self.head = None
    def put(self,key, value):
        new_key = Key(key, value)
        if self.head is None:
           self.head = new_key
           self.tail = new_key
        else:
           self.tail.set_next_node(new_key)
           new_key.set_prev_node(self.tail)
           self.tail = new_key
    def pop(self, key):
        if self.head is None:
            raise KeyError("pop() called without any keys in the hashmap")
        current_node = self.head
        if current_node.get_next_node() is None and str(current_node.get_key()) != key:
                return None
        elif current_node.get_next_node() is None and str(current_node.get_key()) == key:
                self.head = None
                self.tail = None
                return current_node.get_key()
        while current_node:
            if str(current_node.get_key()) == key:

                if current_node.get_prev_node() is None:
                    current_node.get_next_node().set_prev_node(None)
                    self.head = current_node.get_next_node()
                elif current_node.get_next_node() is None:
                    current_node.get_prev_node().set_next_node(None)
                    self.tail = current_node.get_next_node()
                else:
                    prev_node = current_node.get_prev_node()
                    next_node = current_node.get_next_node()
                    prev_node.set_next_node(next_node)
                    next_node.set_prev_node(prev_node)
                return current_node.get_value()
            current_node = current_node.get_next_node()
        return None
    def get(self,key):
        current_node = self.head
        while current_node:
            if current_node.get_key() == key:
                print(current_node.get_value())
            current_node = current_node.get_next_node()

dict = HashMap()
dict.put("a", 1)
dict.put("b", 2)

dict.pop("a")
dict.get("a")
