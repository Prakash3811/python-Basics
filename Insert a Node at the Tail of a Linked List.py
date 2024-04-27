def insertNodeAtTail(head, data):
    if not head:
        return SinglyLinkedListNode(data)
    current = head
    while current.next:
        current = current.next
    current.next = SinglyLinkedListNode(data)
    return head
