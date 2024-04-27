class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructBST(nums):
    root = None
    for num in nums:
        root = insert(root, num)
    return root

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def kthSmallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

n = int(input())
nums = list(map(int, input().split()))
k = int(input())

root = constructBST(nums)

result = kthSmallest(root, k)
print(result)
