"""
Stack implementation in Python. Last in, first out.
Can only add to the top of the stack. Can only remove from the top of the stack.
Can only peek at the top of the stack.
"""

class Node:
    """Node class for queue."""
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

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
    def peek(self):
        return self.tail.get_value()
    def add(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current_tail = self.tail
            current_tail.set_next_node(new_node)
            self.tail = new_node
            self.tail.set_prev_node(current_tail)
    def remove(self):
        if self.tail is None:
            raise ValueError("Cannot remove from empty stack")
        else:
            current_tail = self.tail
            self.tail = current_tail.get_prev_node()
            self.tail.set_next_node(None)
            self.tail.set_prev_node(current_tail)
    def to_list(self):
        """_summary_ converts the Stack class to a list

        Returns:
            list: list of values in the stack
        """
        current_node = self.head
        list_of_values = []
        while current_node:
            list_of_values.append(current_node.get_value())
            current_node = current_node.get_next_node()
        return list_of_values


#Uncomment the following lines to test
# stack = Stack()
# stack.add(1)
# stack.add(3)
# stack.add(5)
# stack.add(7)
# print(stack.to_list())
# stack.remove()
# print(stack.to_list())