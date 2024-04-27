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

n = int(input())
elements = list(map(int, input().split()))
new_number = int(input())


curr = DoublyLinkedList()
for element in elements:
    curr.add_to_tail(element)



curr.print_forward()
curr.print_backward()

curr.add_to_tail(new_number)

curr.print_forward()
curr.print_backward()
print()
