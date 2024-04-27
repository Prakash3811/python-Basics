class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def print_level_order(root):
    if root is None:
        return

    queue = [root]

    while queue:
        print(' '.join(str(node.val) for node in queue))
        queue = [child for node in queue for child in (node.left, node.right) if child]

root = Node(11)
root.left = Node(7)
root.right = Node(15)
root.left.left = Node(5)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(20)
root.left.left.left = Node(3)
root.left.right.left = Node(8)
root.left.right.right = Node(10)
root.right.left.left = Node(12)
root.right.left.right = Node(14)
root.right.right.left = Node(18)
root.right.right.right = Node(25)


print_level_order(root)
