class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    
    curr = head 
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    
    tail = head 
    while tail.next != None:
        tail = tail.next 
        curr = tail
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.prev 
    print()
 
def addNodeAtTailOfLinkedList(head, ele):
    newBlock = Node(ele)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock 
    newBlock.prev = tail 
    return head


def insertAtSpecificPosition(head, position,val):
    newBlock = Node(val)
    if head == None:
        return newBlock
 
    index = 1 
    curr = head 
 
    while index != position-1:
        index += 1 
        curr = curr.next 
    nextNode = curr.next 
    newBlock.next = nextNode 
    nextNode.prev = newBlock 
    curr.next = newBlock 
    newBlock.prev = curr 
    return head


n=int(input()) 
l = map(int,input().split())
pos,val = list(map(int,input().split()))
head = None 
for ele in l:
    head =  addNodeAtTailOfLinkedList(head, ele)
    
printLeftToRightManner(head)
printRightToLeftManner(head)   


head = insertAtSpecificPosition(head, pos,val)
printLeftToRightManner(head)
printRightToLeftManner(head)
