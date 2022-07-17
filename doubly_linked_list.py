
from regex import R


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


class DoublyLinkedList: # REFACTOR: Refactor so that the class keeps track of the count of nodes
    #REFACTOR: Use private methods 
    def __init__(self):
        self.length = 0 #REFACTOR: This should be count
        self.counter = 0
        self.head_node = None
        self.tail_node = None
    def get_head_node(self):
        return self.head_node
    def get_tail_node(self):
        return self.tail_node
    def __set_tail_node(self, new_tail_value):
        new_tail_node = Node(new_tail_value)
        current_tail_node = self.get_tail_node()
        if current_tail_node is None:
            self.head_node = new_tail_node
            self.tail_node = new_tail_node
        else:
            current_tail_node.set_next_node(new_tail_node)
            self.tail_node = new_tail_node
            self.tail_node.set_prev_node(current_tail_node)
    def __set_head_node(self, new_head_value):
        new_head_node = Node(new_head_value)
        current_head_node = self.get_head_node()
        if current_head_node is None:
            self.head_node = new_head_node
            self.tail_node = new_head_node
        else:
            current_head_node.set_prev_node(new_head_node)
            self.head_node = new_head_node
            self.head_node.set_next_node(current_head_node)
        self.length+=1

    def __remove_tail(self):
        current_tail_node = self.get_tail_node()
        if current_tail_node is None:
            raise ValueError("Cannot remove tail from empty doubly linked list")
        if current_tail_node is self.get_head_node():
            self.head_node = None
            self.tail_node = None
        else:
            current_tail_node.get_prev_node().set_next_node(None)
            self.tail_node = current_tail_node.get_prev_node()
        self.length-=1
    def __remove_head(self):
        current_head_node = self.get_head_node()
        if current_head_node is None:
            raise ValueError("Cannot remove head from empty doubly linked list")
        if current_head_node is self.get_tail_node():
            self.head_node = None
            self.tail_node = None
        else:
            current_head_node.get_next_node().set_prev_node(None)
            self.head_node = current_head_node.get_next_node()
        self.length-=1
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
        self.length+=1
    def tail(self):
        return self.tail_node.get_value()
    def insert(self, new_value, index = 0):
        new_node = Node(new_value)
        if self.tail_node is None:
            self.tail_node = new_node
            self.head_node = new_node
        elif index == self.length-1:
            self.__set_tail_node(new_value)
        elif index == 0:
            self.__set_head_node(new_value)#FIXME: This is a bug
            return
        else:
            count = 0
            current_node = self.head_node
            while count != index - 1:
                current_node = current_node.get_next_node()
                count += 1
            current_node.set_next_node(Node(new_value, current_node.get_next_node()))
        self.length+=1
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
        if index == -self.length:
            self.__remove_head()
            return
        self.__assert_integer(index)
        if index == -1:
            tail_node = self.get_tail_node()
            self.__remove_tail()
            return tail_node.get_value()
        if self.head_node is None:
            raise ValueError("The linked list is empty")
        if index < 0:
            current_node = self.tail_node
            if index < -self.length+1:
                raise IndexError("pop index out of range")
            for i in range(-index-1):
                current_node = current_node.get_prev_node()
            self.__remove_node(current_node)
            return
        current_node = self.head_node
        count = 0
        while count != index:
            current_node = current_node.get_next_node()
            count+=1
        self.__remove_node(current_node)
        return current_node.get_value()
    def __remove_node(self, node):
        prev_node = node.get_prev_node()
        next_node = node.get_next_node()
        prev_node.set_next_node(next_node)
        next_node.set_prev_node(prev_node)
        self.length-=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter == 0:
            self.current_node = self.head_node
            self.counter += 1

            return self.get_head_node().get_value()
        while self.current_node.get_next_node() is not None:
            self.current_node = self.current_node.get_next_node()
            return self.current_node.get_value()
        self.counter = 0
        self.current_node = None
        raise StopIteration
    def __assert_integer(self, value):
        #assert that it is an integer
        if not isinstance(value, int):
            raise TypeError("list indices must be integers or slices,not "
                            + str(type(value).__name__))
    def __getitem__(self, item):
        self.__assert_integer(item)
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
        else:
            current_node = self.tail_node
            index = -1
            if index == item:
                return current_node.get_value()
            while current_node.get_next_node():
                index-=1
                if index == item:
                    return current_node.get_next_node().get_value()
                else:
                    current_node = current_node.get_next_node()
            raise IndexError("List index out of range")
    def __setitem__(self,index, value):
        self.__assert_integer(index)
        if index < 0:
            if index * -1 > self.length-1:
                raise IndexError("List assignment index out of range")
            current_node = self.tail_node
            count = -1
            while count != index:
                current_node = current_node.get_prev_node()
                count-=1
            current_node.set_value(value)
        else:
            if index > self.length-1:
                raise IndexError("List assignment index out of range")
            current_node = self.head_node
            count = 0
            while count != index:
                current_node = current_node.get_next_node()
                count+=1
            if current_node is None:
                self.__set_tail_node(value)
                self.length += 1

    def __len__(self): 
        return self.length
    def __str__(self):
        """__summary__: returns a string representation of the linked_list"""
        lst = []
        current_node = self.head_node
        lst.append(current_node.get_value())
        while current_node.get_next_node() is not None:
            lst.append(current_node.get_next_node().get_value())
            current_node = current_node.get_next_node()
        return str(lst)
    def test(self):
        current_node = self.get_tail_node()
        print(current_node.get_value())
        while current_node.get_prev_node() is not None:
            current_node = current_node.get_prev_node()
            print(current_node.get_value())
#Uncomment to test
#Uncomment to test
ll = DoublyLinkedList()
ll.insert(70)
ll.insert(5675)
ll.insert(90)
ll.append(20)
# # ll.swap_nodes(70,5)
# # Added iteration:
# # print(list(ll))
# # for i in ll:
# #     print(i)
# # my_iter_list = iter(ll)
# # for i in ll:
# #     print(i)
print(ll)
ll.pop(-4)
print(ll)
