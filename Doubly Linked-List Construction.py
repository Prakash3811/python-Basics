class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_left_to_right(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def print_right_to_left(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev


if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))

    curr = DoublyLinkedList()

    for value in values:
        curr.insert(value)

    curr.print_left_to_right()
    print()
    curr.print_right_to_left()
