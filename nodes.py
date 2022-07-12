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