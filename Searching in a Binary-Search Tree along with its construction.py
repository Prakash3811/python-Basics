class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_recursive(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert_recursive(node.right, val)
            else:
                node.right = TreeNode(val)

    def search(self, target):
        return self._search_recursive(self.root, target)

    def _search_recursive(self, node, target):
        if not node:
            return False
        if node.val == target:
            return True
        elif target < node.val:
            return self._search_recursive(node.left, target)
        else:
            return self._search_recursive(node.right, target)

def construct_and_search_bst(numbers, target):
    bst = BST()
    for number in numbers:
        bst.insert(number)
    return bst.search(target)

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
found = construct_and_search_bst(numbers, target)

if found:
    print("Target element is found")
else:
    print("Target element is not found")
