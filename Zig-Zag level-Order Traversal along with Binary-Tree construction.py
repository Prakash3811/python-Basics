from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def zigzag_level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_values = []
        level_size = len(queue)

        for _ in range(level_size):
            if left_to_right:
                node = queue.popleft()
                level_values.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                node = queue.pop()
                level_values.append(node.value)
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)

        result.append(level_values)
        left_to_right = not left_to_right

    return result

root = TreeNode(11)
root.left = TreeNode(7)
root.right = TreeNode(15)
root.left.left = TreeNode(5)
root.left.right = TreeNode(9)
root.right.left = TreeNode(13)
root.right.right = TreeNode(20)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(8)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(12)
root.right.left.left = TreeNode(14)
root.right.right.left = TreeNode(18)
root.right.right.right = TreeNode(25)

result = zigzag_level_order_traversal(root)
for level in result:
    print(*level)
