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
                current_node = current_node.get_next_node()
        return string_list
    def swap_nodes(self,value1,value2): #FIXME: should be able to swap nodes in the middle of the list
           node1 = self.head_node
           node2 = self.head_node
           node1_prev = None
           node2_prev = None
 
           while node1 is not None:
             if node1.get_value() == value1:
                break
           node1_prev = node1
           node1 = node1.get_next_node()
           while node2 is not None:
            if node2.get_value() == value2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()
            if node1_prev is None:
                self.head_node = node2
            else:
                node1_prev.set_next_node(node2)
            if node2_prev is None:
                self.head_node = node1
            else:
                node2_prev.set_next_node(node1)
            temp = node1.get_next_node()
            node1.set_next_node(node2.get_next_node())
            node2.set_next_node(temp)
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
ll = LinkedList(0)
for i in range(1,10):
    ll.insert_beginning(i)
print(ll.stringify_list())
ll.swap_nodes(9,5)
print(ll.stringify_list())