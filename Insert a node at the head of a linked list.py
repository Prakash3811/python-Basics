def insertNodeAtHead(llist, data):

    new_node = SinglyLinkedListNode(data)
    new_node.next = llist
    return new_node
