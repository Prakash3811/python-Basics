class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def delete_at_position(self, position):
        if position <= 0 or not self.head:
            print("Invalid position ")
            return

        if position == 1:
            self.head = self.head.next
            return

        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            print("Position out of range")
            return

        current.next = current.next.next

n = int(input())
elements = list(map(int, input().split()))
position = int(input())

sll = SinglyLinkedList()
for element in elements:
    sll.add_to_tail(element)

sll.print_forward()

sll.delete_at_position(position)

sll.print_forward()
print()
