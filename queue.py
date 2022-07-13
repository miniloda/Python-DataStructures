"""Queue implementation in Python. First in, first out.
Can only add to the end of the queue. Can only remove from the front of the queue.
Can only peek at the front of the queue.
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

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def peek(self):
        return self.head.get_value()
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            new_node.set_prev_node(self.tail)
            self.tail = new_node
    def dequeue(self):
        """_summary_ removes the head of the queue

        Raises:
            ValueError: _description_
        """
        if self.head is None:
            raise ValueError("Cannot dequeue from empty queue")
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            current_head = self.head
            self.head = current_head.get_next_node()
            self.head.set_prev_node(None)
    def to_list(self):
        """_summary_ converts the Queue class to a list

        Returns:
            list: list of values in the queue
        """
        current_node = self.head
        list_of_values = []
        while current_node:
            list_of_values.append(current_node.get_value())
            current_node = current_node.get_next_node()
        return list_of_values
#Uncomment to test code
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.dequeue()
# print(queue.to_list())
# print(queue.peek())