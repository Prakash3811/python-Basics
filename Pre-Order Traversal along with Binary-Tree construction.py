class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node:
        print(node.value, end = " ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

node11 = TreeNode(11)
node7 = TreeNode(7)
node5 = TreeNode(5)
node3 = TreeNode(3)
node9 = TreeNode(9)
node8 = TreeNode(8)
node10 = TreeNode(10)
node15 = TreeNode(15)
node13 = TreeNode(13)
node12 = TreeNode(12)
node14 = TreeNode(14)
node20 = TreeNode(20)
node18 = TreeNode(18)
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
node13.right = node12
node12.left = node14
node20.right = node18
node18.right = node25


preorder_traversal(node11)
