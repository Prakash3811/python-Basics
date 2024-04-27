class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

    def delete_at_position(self, position):
        if position < 1:
            print("Invalid position")
            return
        elif position == 1:
            if self.head:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            else:
                print("List is empty")
            return

        current = self.head
        count = 1
        while current and count != position:
            current = current.next
            count += 1

        if not current:
            print("Position out of range")
            return

        if current == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

n = int(input())
elements = list(map(int,input().split()))

position=int(input())


cur = DoublyLinkedList()
for element in elements:
    cur.add_to_tail(element)


cur.print_forward()
cur.print_backward()
cur.delete_at_position(position)

cur.print_forward()
cur.print_backward()
print()
