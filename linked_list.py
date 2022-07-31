"""LinkedList implementation in Python."""

# We'll be using our Node class


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
        self.counter = 0
        self.current_node = None
        self.head_node = Node(value)
    def __str__(self):
        """__summary__: returns a string representation of the linked_list"""
        lst = []
        current_node = self.head_node
        lst.append(current_node.get_value())
        while current_node.get_next_node() is not None:
            lst.append(current_node.get_next_node().get_value())
            current_node = current_node.get_next_node()
        return str(lst)
    def get_head_node(self):
        return self.head_node
    def insert(self, new_value, index = 0):
        if index == 0:
            self.head_node = Node(new_value, self.head_node)
        else:
            count = 0
            current_node = self.head_node
            while count != index - 1:
                current_node = current_node.get_next_node()
                count += 1
            current_node.set_next_node(Node(new_value, current_node.get_next_node()))
    def append(self, new_value):# Not good for large lists, use doubly linked list instead
        current_node = self.head_node
        while current_node.get_next_node():
            current_node = current_node.get_next_node()
        current_node.set_next_node(Node(new_value))
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
        return string_list
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter == 0:
            self.current_node = self.head_node
            self.counter += 1
            return self.get_head_node().get_value()
        while self.current_node.get_next_node():
            self.current_node = self.current_node.get_next_node()
            return self.current_node.get_value()
        self.counter = 0
        self.current_node = None
        raise StopIteration  # signals "the end"
    # def swap_nodes(self,value1,value2):
    #     value_1_prev = None
    #     value_2_prev = None
    #     if self.get_head_node() is None:
    #         return
    #     current_node = self.get_head_node()
    #     #If the current head is the one to be swapped, we should set the swapped value to be the new head
    #     if self.get_head_node().get_value() == value1:
    #         value_1_node = self.get_head_node()
    #         value_1_next = self.get_head_node().get_next_node()
    #     elif self.get_head_node().get_value() == value2:
    #         value_2_node = self.get_head_node() # else:
        #     current_node = self.tail_node
        #     index = -1
        #     if index == item:
        #         return current_node.get_value()
        #     while current_node.get_next_node():
        #         index-=1
        #         if index == item:
        #             return current_node.get_next_node().get_value()
        #         else:
        #             current_node = current_node.get_next_node()
        #     raise IndexError("List index out of range")e().get_next_node()
        #     elif current_node.get_next_node().get_value() == value2:
        #         value_2_node = current_node.get_next_node()
        #         value_2_prev = current_node
        #         value_2_next = current_node.get_next_node().get_next_node()
        #     current_node = current_node.get_next_node()
        # try:
        #     if value_1_node is None or value_2_node is None:
        #         print("One of the nodes is not in the list")
        # except UnboundLocalError:
        #     print("One of the nodes is not in the list")
        #     return
        #       # Add extra code to keep track of the head of the list
        # if value_1_node == self.get_head_node():
        #     prev_head_node = self.get_head_node()
        #     self.head_node = value_2_node
        #     self.head_node.set_next_node(prev_head_node.get_next_node())
        #     value_1_node.set_next_node(value_2_next)
        #     value_2_prev.set_next_node(value_1_node)
        # elif value_2_node is self.get_head_node():
        #     prev_head_node = self.get_head_node()
        #     self.head_node = value_1_node
        #     self.head_node.set_next_node(prev_head_node.get_next_node())
        #     value_2_node.set_next_node(value_1_next)
        #     value_1_prev.set_next_node(value_2_node)
        # else:
        #     value_1_prev.set_next_node(value_2_node)
        #     value_2_prev.set_next_node(value_1_node)
        #     temp_node = value_1_node.get_next_node()
        #     value_1_node.set_next_node(value_2_node.get_next_node())
        #     value_2_node.set_next_node(temp_node)
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
    def pop(self, index = 0):
        """The pop() method removes the item at the given index from the list and returns the removed item.
        The method returns the value of the last item in the list if no index is specified.
        If the list is empty, the method raises a ValueError exception.
        """
        count = 0
        if self.head_node is None:
            raise ValueError("The list is empty")
        current_node = self.head_node
        while count != index:
            current_node = current_node.get_next_node()
        self.remove_node(current_node.get_value())
        return current_node.get_value()
    def __getitem__(self, item):
        if item >= 0:
            current_node = self.get_head_node()
            index = 0
            if index == item:
                return current_node.get_value()
            while current_node.get_next_node():
                index+=1
                if index == item:
                    return current_node.get_next_node().get_value()
                else:
                    current_node = current_node.get_next_node()
            raise IndexError("List index out of range")
        # else:
        #     current_node = self.tail_node
        #     index = -1
        #     if index == item:
        #         return current_node.get_value()
        #     while current_node.get_next_node():
        #         index-=1
        #         if index == item:
        #             return current_node.get_next_node().get_value()
        #         else:
        #             current_node = current_node.get_next_node()
        #     raise IndexError("List index out of range")

#Uncomment to test
# ll = LinkedList(5)
# ll.insert(70)
# ll.insert(5675)
# ll.insert(90)
# ll.append(20)
# # print(ll.stringify_list())
# # ll.swap_nodes(70,5)
# # Added iteration:
# print(list(ll))
# for i in ll:
#     print(i)
# my_iter_list = iter(ll)

