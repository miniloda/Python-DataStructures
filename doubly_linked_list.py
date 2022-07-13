
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
    def to_list(self):
        current_node = self.get_head_node()
        list_of_values = []
        while current_node:
            list_of_values.append(current_node.get_value())
            current_node = current_node.get_next_node()
        return list_of_values
    def remove_tail(self):
        current_tail_node = self.get_tail_node()
        if current_tail_node is None:
            raise ValueError("Cannot remove tail from empty doubly linked list")
        if current_tail_node is self.get_head_node():
            self.head_node = None
            self.tail_node = None
        else:
            current_tail_node.get_prev_node().set_next_node(None)
            self.tail_node = current_tail_node.get_prev_node()
    def remove_head(self):
        current_head_node = self.get_head_node()
        if current_head_node is None:
            raise ValueError("Cannot remove head from empty doubly linked list")
        if current_head_node is self.get_tail_node():
            self.head_node = None
            self.tail_node = None
        else:
            current_head_node.get_next_node().set_prev_node(None)
            self.head_node = current_head_node.get_next_node()
    def append(self, tail_node):
        new_tail_node = Node(tail_node)
        current_tail_node = self.get_tail_node()
        if current_tail_node is None:
            self.tail_node = new_tail_node
            self.head_node = new_tail_node
        else:
            current_tail_node.set_next_node(new_tail_node)
            self.tail_node = new_tail_node
            self.tail_node.set_prev_node(current_tail_node)
    def insert(self, index, value):
        if index == 0:
            self.set_head_node(value)
        else:
            current_node = self.head_node
            count = 0
            while count != index:
                if current_node.get_next_node() is None:
                    self.append(value)
    def pop(self, index = -1):
        """__summary__: removes the item at the given index from the list and returns the removed item.
        The method returns the value of the last item in the list if no index is specified.
        Args:
            index(int): the index of the item to be removed, default is -1
        Returns:
            value: the value of the removed item
        Throws:
            ValueError: if the index is out of range
        """
        count = 0
        if index == -1:
            tail_node = self.get_tail_node()
            self.remove_tail()
            return tail_node.get_value()
        if self.head_node is None:
            raise ValueError("The linked list is empty")
        current_node = self.head_node
        while count != index:
            current_node = current_node.get_next_node()
            count+=1
        self.remove_node(current_node)
        return current_node.get_value()
    def remove_node(self, node):
        prev_node = node.get_prev_node()
        next_node = node.get_next_node()
        prev_node.set_next_node(next_node)
        next_node.set_prev_node(prev_node)

#Uncomment to test
dll = DoublyLinkedList()
print(dll.to_list())
