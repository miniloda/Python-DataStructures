"""LinkedList implementation in Python."""

# We'll be using our Node class
from tomlkit import value


class Node:
    """Node class for linked list."""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
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

# Our LinkedList class
class LinkedList:
    """LinkedList class for linked list."""
    def __init__(self, value=None):
        self.head_node = Node(value)
    def get_head_node(self):
        return self.head_node
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
                print(current_node.get_value())
                current_node = current_node.get_next_node()
        return string_list
    def swap_nodes(self,value1,value2): #FIXME: should be able to swap nodes in the middle of the list
        if self.get_head_node() is None:
            return
        current_node = self.get_head_node()
        #If the current head is the one to be swapped, we should set the swapped value to be the new head
        if self.get_head_node().get_value() == value1:
            value_1_node = self.get_head_node()
            value_1_next = self.get_head_node().get_next_node()
        elif self.get_head_node().get_value() == value2:
            value_2_node = self.get_head_node()
            value_2_next = self.get_head_node().get_next_node()
        while current_node.get_next_node() is not None:
            if current_node.get_next_node().get_value() == value1:
                value_1_node = current_node.get_next_node()
                value_1_prev = current_node
                value_1_next = current_node.get_next_node().get_next_node()
            elif current_node.get_next_node().get_value() == value2:
                value_2_node = current_node.get_next_node()
                value_2_prev = current_node
                value_2_next = current_node.get_next_node().get_next_node()
            current_node = current_node.get_next_node()
        try:
            if value_1_node is None or value_2_node is None:
                print("One of the nodes is not in the list")
        except UnboundLocalError:
            print("One of the nodes is not in the list")
            return
              # Add extra code to keep track of the head of the list
        if value_1_node == self.get_head_node():
            prev_head_node = self.get_head_node()
            self.head_node = value_2_node
            self.head_node.set_next_node(prev_head_node.get_next_node())
            value_1_node.set_next_node(value_2_next)
            value_2_prev.set_next_node(value_1_node)
        elif value_2_node is self.get_head_node():
            prev_head_node = self.get_head_node()
            self.head_node = value_1_node
            self.head_node.set_next_node(prev_head_node.get_next_node())
            value_2_node.set_next_node(value_1_next)
            value_1_prev.set_next_node(value_2_node)
        else:
            value_1_prev.set_next_node(value_2_node)
            value_2_node.set_next_node(value_1_next)
            value_2_prev.set_next_node(value_1_node)
            value_1_node.set_next_node(value_2_next)
  # Define your remove_node method below:
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node.get_next_node():
                if current_node.get_next_node().get_value() == value_to_remove:
                    linked_node = current_node.get_next_node().get_next_node()
                    current_node.set_next_node(linked_node)
                    break
            else:
                current_node = current_node.get_next_node()
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)