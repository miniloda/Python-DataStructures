from linked_list import LinkedList

def reverse_linked_list(linkedlist):
    head = linkedlist.head_node
    if head is None:
        return None
    elif head.next_node is None:
        return head
    prev_node = None
    current_node = head
    next_node = head.next_node
    while current_node.next_node:
        current_node.next_node = prev_node
        prev_node = current_node
        holder = next_node
        current_node = holder
        next_node = current_node.next_node
    current_node.next_node = prev_node
    linkedlist.head_node = current_node

# ll = LinkedList(5)
# ll.insert(70)
# ll.insert(5675)
# ll.insert(90)
# ll.append(20)
# print(ll)
# reverse_linked_list(ll)
# print("Reversed link: "+ str(ll))