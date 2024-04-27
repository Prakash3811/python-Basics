class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next

def construct_linked_list(n, values):
    linked_list = LinkedList()
    for value in values:
        linked_list.insert(value)
    return linked_list

n = int(input())  
values = list(map(int, input().split())) 
linked_list = construct_linked_list(n, values)
linked_list.print_list()

