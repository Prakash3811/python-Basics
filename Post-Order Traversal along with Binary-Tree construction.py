class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")

node3 = TreeNode(3)
node5 = TreeNode(5)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node11 = TreeNode(11)
node12 = TreeNode(12)
node13 = TreeNode(13)
node14 = TreeNode(14)
node15 = TreeNode(15)
node18 = TreeNode(18)
node20 = TreeNode(20)
node25 = TreeNode(25)

node11.left = node7
node11.right = node15
node7.left = node5
node7.right = node9
node5.left = node3
node9.left = node8
node9.right = node10
node15.left = node13
node15.right = node20
node13.left = node12
node13.right = node14
node20.left = node18
node20.right = node25



postorder_traversal(node11)
