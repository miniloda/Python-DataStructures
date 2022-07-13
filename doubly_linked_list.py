class Node:
    """Node class for doubly linked list."""
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = None
    def get_value(self):
        """_summary_ gets the value of this node
        Returns:
            value: the value of this node
        """
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, next_node):
        self.next_node = next_node
    def get_prev_node(self):
        return self.prev_node
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    def get_head_node(self):
        return self.head_node
    def get_tail_node(self):
        return self.tail_node
    def set_head_node(self, new_head_value):
        new_head_node = Node(new_head_value)
        current_head_node = self.get_head_node()
        if current_head_node is None:
            self.head_node = new_head_node
            self.tail_node = new_head_node
        else:
            current_head_node.set_prev_node(new_head_node)
            self.head_node = current_head_node
            self.head_node.set_next_node(current_head_node)
    def set_tail_node(self, tail_node):
        new_tail_node = Node(tail_node)
        current_tail_node = self.get_tail_node()
        if current_tail_node is None:
            self.tail_node = new_tail_node
            self.head_node = new_tail_node
        else:
            current_tail_node.set_next_node(new_tail_node)
            self.tail_node = new_tail_node
            self.tail_node.set_prev_node(current_tail_node)
    def to_list(self):
        current_node = self.get_head_node()
        list_of_values = []
        while current_node:
            list_of_values.append(current_node.get_value())
            current_node = current_node.get_next_node()
        return list_of_values

#Uncomment to test
# dll = DoublyLinkedList()
# dll.set_head_node(1)
# dll.set_tail_node(2)
# print(dll.toList())